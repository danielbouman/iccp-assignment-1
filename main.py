## Import modules
import numpy as np		
import matplotlib.pyplot as plt 			# plotting tools
from mpl_toolkits.mplot3d import Axes3D		# plotting tools
import save_data as save                    # data export for physcial quantities
import initialize as init                   # initialize particles
import phys_quantities as phys              # determine physical quantities
from velocity_verlet import velocity_verlet # velocity verlet, used for time evolution of the particles
from normalize_momentum import normalize_momentum  
import running as start                     # startup message

## Global settings
np.set_printoptions(threshold='nan')		# Do not truncate print

## User input
rho = raw_input('Density (in units of 1/sigma^3, default: 0.88): ') or 0.88  # Density, N/V
T_d = raw_input('Desired temperature (default: 1): ') or 1                   # In units of timesteps
plot_data = raw_input('Plot data? (y/n, default: y): ') or 'y'               # Option to plot data after simulation 
time_dur = raw_input('Timesteps: ') or 1600                                   # Duration of the simulation in timesteps

## Assign variables
#L = 4.969                  # Box length
M = 2                       # Unit cells per dimension
N = 4*np.power(M,3)         # Number of particles, 4 per unit cell
h = 0.004                   # Timestep
#T_d = 119.8                # desired temperature
r_c = 62.5                  # Cut off length in terms of L
rho = float(rho)            # make sure rho is a float
L = np.power((N/rho),(float(1)/3))  # get vertex length L of the volume
T_d = float(T_d)            # make sure desired temperature is a float
time_dur = int(time_dur)    # make sure timesteps is an integer value
t_equil = 200              # duration of equilibration phase

## Message at simulation start
start.message()

## Assign empty arrays to variables used in entire simulation, adjust range to number of array
time_step, vel_time, pos_time, time, kin_energy, total_velocity,\
    mean_P, T, D, pot_energy, total_energy, P, specific_heat_1, \
    specific_heat_2, time_step_phys = (np.zeros((time_dur),dtype=float) for i in range(15))
## Assign empty arrays to physical quantities in equilibrium phase
# if time_dur > t_equil:
#         = (np.zeros((time_dur-t_equil),dtype=float) for i in range(6))

t_prog = 0                                                  # countdown timer
n_bins = 1000                                               # histogram bins, used for correlation function
dist_hist = np.zeros((n_bins-1,time_dur),dtype=float)       # actual histogram, used for correlation function
max_pair_dis = 0.5*np.power(3,0.5)*L                        # Maximum pair distance, used for correlation length calculation
hist_bins = np.linspace(0,max_pair_dis,num=n_bins)          # histogram bins, used for correlation length
delta_r = max_pair_dis/n_bins

## Initialize system
pos = init.position( L,N,M )            # position
velocity = init.momentum( N, T_d)       # momentum
a_0 = np.zeros((N,3),dtype=float)       # acceleration

## Time evolution
for t in xrange(0, time_dur):
    
    ## Equilibration phase
    time_step[t] = t
    ## Velocity verlet
    pos,velocity,a_0,potential,virial,dist_hist[:,t],D[t] = velocity_verlet( N, h, pos, velocity, a_0, L, r_c, hist_bins)
    ## Kinetic energy
    kin_energy[t] = sum(sum(0.5*(np.power(velocity,2))))
    ## Intantanious temperature
    T[t] = (float(2)/(3*(N-1)))*float(kin_energy[t])
    ## Normalize momentum (with rescaling)
    if np.mod(t,40) == 0 and t<=201:
        velocity = normalize_momentum(N,velocity,T_d,kin_energy[t])
        
    ## Equilibrium phase
    if t>t_equil:
        pot_energy[t] = (0.5*sum(potential))/N                  # Potential energy per particle. Factor 0.5 to avoid double counting
        total_energy[t] = np.add(kin_energy[t],pot_energy[t])   # Total energy
        P[t] = (phys.pressure(T[t],N,L,virial,r_c))/(T[t]*rho)  # Pressure
        specific_heat_1[t], specific_heat_2[t] = phys.specific_heat(N,T[t],total_energy[t-50:t],kin_energy[t-50:t])     # Specific heat
        correlation_function = np.divide( ((2*np.power(L,3))/(N*(N-1)))*(np.mean(dist_hist,axis=1))/(4*np.pi*delta_r),np.power(np.multiply(hist_bins[1:],0.5),2))   # correlation function
        #mean_P[t] = np.mean(P[t-100:t])
        
    ## Simulation progress
    if np.mod(t,time_dur/10) == 0:
        print str(10-t_prog)
        t_prog = t_prog+1

## Save physical quantities
save.save(kin_energy,"kinetic_enery",write_mode="w")
save.save(T,"instant_temperature",write_mode="w")
save.save(pot_energy,"potential_energy",write_mode="w")
save.save(P,"pressure",write_mode="w")
save.save(total_energy,"total_energy",write_mode="w")
if time_dur >= t_equil: 
    save.save(correlation_function,"correlation_function",write_mode="w")

## Plot data
if plot_data == 'y':
    # plt.show()
    # plt.plot(time_step,T, 'b')
    # plt.show()
    # plt.plot(time_step,specific_heat_1, 'b')
    # plt.show()
    # plt.plot(time_step,specific_heat_2, 'b')
    # plt.show()
    plt.plot(time_step,D*5.32E-8, 'g')
    plt.show()
    # plt.plot(time_step,kin_energy, 'r', time_step,pot_energy, 'b',time_step,total_energy,'g')
    # plt.show()
    ## Plot physical quantities only when system was in equilibrium
    if time_dur >= t_equil:
        # plt.plot(time_step,P,'k',time_step,mean_P,'b')
        # plt.show()
        # plt.plot(time_step,pot_energy, 'b')
        # plt.show()
        # plt.plot(time_step,D, 'b')
        # plt.show()
        plt.plot(time_step,specific_heat_2, 'b')
        plt.show()
