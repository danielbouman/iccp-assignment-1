## Import libraries
import numpy as np 							
import matplotlib.pyplot as plt 			# plotting tools
from mpl_toolkits.mplot3d import Axes3D		# plotting tools
np.set_printoptions(threshold='nan')		# Do not truncate
import re 									# string edit tools
import time 								# timing tools
## Import functions
from initpos_function import initpos
from initvelocity import initvelocity
from velocity_verlet import velocity_verlet
from normalize_momentum import normalize_momentum
from store_quantities import store_quantities
from pressure import virial_pressure
from specific_heat import specific_heat
from running_text import running_text

## Assign variables
#L = 4.969                      # Box length
M = 2                       # Unit cells per dimension
N = 4*np.power(M,3)         # Number of particles, 4 per unit cell
h = 0.004                   # Timestep
#T_d = 119.8                   # desired temperature
r_c = 62.5                  # Cut off length in terms of L

rho = raw_input('Insert desired density (in units of 1/sigma^3: ') or 0.88
T_d = raw_input('Insert desired temperature: ') or 1         # In units of timesteps
display_data = raw_input('Write to file (w) or plot (p): ') or 'p'
time_dur = raw_input('Timesteps: ') or 400         # In units of timesteps
rho = float(rho)
L = np.power((N/rho),(float(1)/3))
T_d = float(T_d)
time_dur = int(time_dur)

running_text()

time_step = np.zeros((time_dur),dtype=float)
vel_time = np.zeros((time_dur),dtype=float)
pos_time = np.zeros((time_dur),dtype=float)
time = np.zeros((time_dur),dtype=float)
kin_energy = np.zeros((time_dur),dtype=float)
total_velocity = np.zeros((time_dur),dtype=float)
pot_energy = np.zeros((time_dur),dtype=float)
total_energy = np.zeros((time_dur),dtype=float)
P = np.zeros((time_dur),dtype=float)
mean_P = np.zeros((time_dur),dtype=float)
T = np.zeros((time_dur),dtype=float)
specific_heat_1 = np.zeros((time_dur),dtype=float)
specific_heat_2 = np.zeros((time_dur),dtype=float)
diffusion_constant = np.zeros((time_dur),dtype=float)
exp_n = np.zeros((time_dur),dtype=float)
t_prog = 0
n_bins = 1000
dist_hist = np.zeros((n_bins,time_dur),dtype=float)
max_pair_dis = 0.5*np.power(3,0.5)*L                        # Maximum pair distance, used for correlation length calculation
hist_bins = np.linspace(0,max_pair_dis,num=n_bins)          # histogram bins, used for correlation length
delta_r = max_pair_dis/n_bins

## Init particle positions
pos = initpos( L,N,M )

## Init velocity
velocity = initvelocity( N, T_d)

## Init acceleration
a_0 = np.zeros((N,3),dtype=float) #Initialize acceleration array

## Plotting
# fig = plt.figure()  # Define figure

## Time evolution
for t in xrange(0, time_dur):
    pos,velocity,a_0,potential,virial,dist_hist[:,t] = velocity_verlet( N, h, pos, velocity, a_0, L, r_c, hist_bins)
    time_step[t] = t
    pot_energy[t] = 0.5*sum(potential)
    kin_energy[t] = sum(sum(0.5*(np.power(velocity,2))))
    
    T[t] = (float(2)/(3*(N-1)))*float(kin_energy[t])
    total_energy[t] = np.add(kin_energy[t],pot_energy[t])
    P[t] = (virial_pressure(T[t],N,L,virial,r_c))/(T[t]*rho)
    if np.mod(t,40) == 0 and t<=801:
        velocity = normalize_momentum(N, velocity,T_d)
    if t>100:
        specific_heat_1[t], specific_heat_2[t] = specific_heat(N,T[t],total_energy[t-50:t],kin_energy[t-50:t])
        mean_P[t] = np.mean(P[t-100:t])
        #print "sp1"
        #print specific_heat_1
        #print "sp2"
        #print specific_heat_2
        # Print progress
    if np.mod(t,time_dur/10) == 0:
        print str(10-t_prog)
        t_prog = t_prog+1

correlation_length = np.divide( ((2*np.power(L,3))/(N*(N-1)))*(np.mean(dist_hist,axis=1))/(4*np.pi*delta_r), hist_bins[1:-1]) #KWADRATEREN
print correlation_length

out_energ = str(total_energy) + "\n"
out_energ = re.sub(' +',' ',out_energ)
out_energ = out_energ.translate(None, '[]').replace(" ", "\n")
with open("total_energy.dat", "w") as f_energ:
	f_energ.write(out_energ)
f_energ.close()
out_kin = str(kin_energy) + "\n"
out_kin = re.sub(' +',' ',out_kin)
out_kin = out_kin.translate(None, '[]').replace(" ", "\n")
with open("kin_energy.dat", "w") as f_kin:
	f_kin.write(out_kin)
f_kin.close()
out_pot = str(pot_energy) + "\n"
out_kin = re.sub(' +',' ',out_kin)
out_pot = out_pot.translate(None, '[]').replace(" ", "\n")
with open("pot_energy.dat", "w") as f_pot:
	f_pot.write(out_pot)
f_pot.close()
instant_temp = str(T) + "\n"
instant_temp = re.sub(' +',' ',instant_temp)
instant_temp = instant_temp.translate(None, '[]').replace(" ", "\n")
with open("instant_temp.dat", "w") as f_temp:
	f_temp.write(instant_temp)
f_temp.close()
pressure = str(P) + "\n"
pressure = re.sub(' +',' ',pressure)
pressure = pressure.translate(None, '[]').replace(" ", "\n")
with open("pressure.dat", "w") as f_pres:
	f_pres.write(pressure)
f_pres.close()

if display_data == 'p':
    # plt.show()
    # plt.plot(time_step,T, 'b')
    # plt.show()
    # plt.plot(time_step,specific_heat_1, 'b')
    # plt.show()
    # plt.plot(time_step,specific_heat_2, 'b')
    # plt.show()
    # plt.plot(time_step,diffusion_constant, 'g')
    # plt.show()
    # plt.plot(time_step,kin_energy, 'r', time_step,pot_energy, 'b',time_step,total_energy,'g')
    # plt.show()
    plt.plot(time_step,P,'k',time_step,mean_P,'b')
    plt.show()
    plt.plot(time_step,pot_energy, 'b')
    plt.show()
    print exp_n
    # plt.plot(time_step,total_energy, 'b')