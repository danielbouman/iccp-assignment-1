## Import libraries
import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold='nan')
import datetime
## Import functions
from initpos_function import initpos
from initvelocity import initvelocity
from velocity_verlet import velocity_verlet
from normalize_momentum import normalize_momentum
from store_quantities import store_quantities
## Assign variables
L = 20                      # Box length
M = 1                       # Unit cells per dimension
N = 4*np.power(M,3)         # Number of particles, 4 per unit cell
h = 0.01 					# Timestep
T = 300                     # Temperature
m = 1                       # Particle mass
time_dur = 1000            # In units of timesteps
vel_time = pos_time = \
time = kin_energy = \
total_velocity = pot_energy = \
total_energy = np.zeros((time_dur,1),dtype=float)

## Init particle positions
pos = initpos( L,N,M )

## Init velocity
velocity = initvelocity( N, T ,m )

## Init acceleration
a_0 = np.zeros((N,3),dtype=float) #Initialize acceleration array

## Write timestamp to output file
time = datetime.datetime.now()
with open("output.dat", "a") as fh:
    fh.write("\n# "+time.strftime('%Y/%m/%d %H:%M:%S')+":\n\n")
    fh.write("Velocity 1\n")
    
## Plotting
# fig = plt.figure()  # Define figure
    
## Time evolution
for t in xrange(0, time_dur):
    pos,velocity,a_0,potential = velocity_verlet( N, h, pos, velocity, a_0, L )
    pot_energy[t] = sum(potential)
    (kin_energy[t],total_velocity[t]) = store_quantities(N,velocity)
    if np.mod(t,200) = 0:
    	velocity = normalize_momentum(N, velocity,T)
    	
    #total_energy[t] = np.add(kin_energy,pot_energy)
    ## Dynamic plotting
    # time[t] = t 
    # pos_time[t] = pos[0,1]
    # plt.xlim([0,L])
    # plt.ylim([0,L])
    # plt.show()
    # ax = Axes3D(fig)                            # Define axis
    # ax.scatter(pos[:,0], pos[:,1], pos[:,2])    # Plot positions#
    ## Print
    # print velocity[0,0]
    # print kin_energy[t]
    # print pos[1,2]
    ## Write to output file
    # out_vel = str(pot_energy[1,2]) + "\n"
    # with open("output.dat", "a") as fh:
    #     fh.write(out_vel)
    
    out_val = str(total_energy[t]) + "\n"
    out_val = out_val.translate(None, '[]').replace(" ", "")
    with open("output.dat", "a") as fh:
        fh.write(out_val)
fh.close() # Close output file

## Plotting
# plt.plot(time,pot_energy, 'r')
# plt.show()
# plt.plot(time,kin_energy, 'b')
# plt.show()
# plt.plot(time,total_energy, 'g')
# plt.show()
# plt.plot(time,pot_energy,'g')