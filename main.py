"""
This program simulates an argon gas. The user can specify the particle density and desired temperature. The program will return
the diffusion constant, specific heat, temperature, pressure, correlation length, potential-, kinetic- and total energy.
"""

## Import modules
from __future__ import print_function       # make print function work in older versions of python
import numpy as np		
import matplotlib.pyplot as plt 			# plotting tools
from mpl_toolkits.mplot3d import Axes3D		# plotting tools
import save_data as save                    # data export for physcial quantities
import initialize as init                   # initialize particles
import phys_quantities as phys              # determine physical quantities
from velocity_verlet import velocity_verlet # velocity verlet, used for time evolution of the particles
from normalize_momentum import normalize_momentum  
import running as start                     # startup message
import statistical as stat                  # determine statistical propertie and save to file
import sys                                  # progress messages

## Global settings
np.set_printoptions(threshold='nan')		# Do not truncate print

## User input
# Fix Python 2.x.
try: input = raw_input
except NameError: pass
rho = input('Density (in units of 1/sigma^3, default: 0.88): ') or 0.88  # Density, N/V
T_d = input('Desired temperature (default: 1): ') or 1                   # In units of timesteps
plot_data = input('Plot data? (y/n, default: y): ') or 'y'               # Option to plot data after simulation 
time_dur = input('Timesteps: ') or 1600                                  # Duration of the simulation in timesteps

## Assign variables
M = 3                       # Unit cells per dimension
N = 4*np.power(M,3)         # Number of particles, 4 per unit cell
h = 0.004                   # Timestep
r_c = 62.5                  # Cut off length in terms of L
rho = float(rho)            # make sure rho is a float
L = np.power((N/rho),(float(1)/3))  # get vertex length L of the volume
T_d = float(T_d)            # make sure desired temperature is a float
time_dur = int(time_dur)    # make sure timesteps is an integer value
t_equil = 2500              # duration of equilibration phase
other_quantities = "Rho: "+str(rho)+", T_d: "+str(T_d)+", N: "+str(N)+", Runtime: "+str(time_dur)

## Message at simulation start
start.message()

## Assign empty arrays to variables used in entire simulation, adjust range to number of array
time_step, vel_time, pos_time, time, kin_energy, total_velocity,\
    mean_P, T, D, pot_energy, total_energy, P, sp_heat, \
    time_step_phys = (np.zeros((time_dur),dtype=float) for i in range(14))
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
for t in range(0, time_dur):
    
    ## Equilibration phase
    time_step[t] = t
    ## Velocity verlet
    pos,velocity,a_0,potential,virial,dist_hist[:,t],D[t] = velocity_verlet( N, h, pos, velocity, a_0, L, r_c, hist_bins)
    ## Kinetic energy
    kin_energy[t] = sum(sum(0.5*(np.power(velocity,2))))
    ## Intantanious temperature
    T[t] = (float(2)/(3*(N-1)))*float(kin_energy[t])
    ## Normalize momentum (with rescaling)
    if np.mod(t,40) == 0 and t<=1201:
        velocity = normalize_momentum(N,velocity,T_d,kin_energy[t])
        
    ## Equilibrium phase
    if t>t_equil:
        pot_energy[t] = (0.5*sum(potential))/N                  # Potential energy per particle. Factor 0.5 to avoid double counting
        total_energy[t] = np.add(kin_energy[t],N*pot_energy[t])   # Total energy in the system
        P[t] = (phys.pressure(T[t],N,L,virial,r_c))/(T[t]*rho)  # Pressure
        sp_heat[t] = phys.specific_heat(N,T[t],kin_energy[t-50:t])     # Specific heat
        correlation_function = np.divide( ((2*np.power(L,3))/(N*(N-1)))*(np.mean(dist_hist,axis=1))/(4*np.pi*delta_r),np.power(np.multiply(hist_bins[1:],0.5),2))   # correlation function
        
    ## Simulation progress
    if np.mod(t,time_dur/100) == 0:
        # print ('%d%%' % t_prog)
        sys.stdout.write("Progress: %d%%   \r" % (t_prog) )
        sys.stdout.flush()
        t_prog = t_prog+1

## Save physical quantities
save.save(kin_energy,"kinetic_enery",write_mode="w")
save.save(T,"instant_temperature",write_mode="w")
save.save(pot_energy,"potential_energy",write_mode="w")
save.save(P,"pressure",write_mode="w")
save.save(total_energy,"total_energy",write_mode="w")
save.save(sp_heat,"specific_heat",write_mode="w")
save.save(D,"diffustion_constant",write_mode="w")
if time_dur >= t_equil: 
    save.save(correlation_function,"correlation_function",write_mode="w")
    stat.save_phys(T[t_equil+1:],"Temperature",True,other_quantities)
    stat.save_phys(P[t_equil+1:],"Pressure")
    stat.save_phys(pot_energy[t_equil+1:],"Potential")
    stat.save_phys(sp_heat[t_equil+1:],"Specif_heat")
    stat.save_phys(total_energy[t_equil+1:],"Tot_energy")
    stat.save_phys(D[t_equil+1:],"diffusion")

## Plot data
if plot_data == 'y':
    plt.plot(time_step,D*5.32E-8, 'g')                          # Scale factor of 5.32E-8 to revert back to standard non-reduced units, m^2/s
    plt.show()
    ## Plot physical quantities only when system was in equilibrium
    if time_dur >= t_equil:
        plt.plot(time_step,sp_heat, 'b')
        plt.show()
