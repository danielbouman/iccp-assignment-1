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
M = 2                       # Unit cells per dimension
N = 4*np.power(M,3)         # Number of particles, 4 per unit cell
h = 0.0004 					# Timestep
T = 300                     # Temperature
m = 1                       # Particle mass

## Init particle positions
pos = initpos( L,N,M )

## Init velocity
velocity = initvelocity( N, T ,m )

## Init acceleration
a_0 = np.zeros((N,3),dtype=float) #Initialize acceleration array

## Velocity verlet
#vel_time = np.array([])
vel_time = np.zeros((100,1),dtype=float)
pos_time = np.zeros((100,1),dtype=float)
time = np.zeros((100,1),dtype=float)
kin_energy = np.zeros((100,1),dtype=float)
total_velocity = np.zeros((100,1),dtype=float)
pot_energy = np.zeros((100,1),dtype=float)

## Write timestamp to output file
time = datetime.datetime.now()
with open("output.dat", "a") as fh:
    fh.write("\n# "+time.strftime('%Y/%m/%d %H:%M:%S')+":\n\n")
    fh.write("Velocity 1\n")
    
## Plotting
# fig = plt.figure()  # Define figure
    
## Time evolution
for t in xrange(0, 10):
    pos,velocity,a_0,potential = velocity_verlet( N, h, pos, velocity, a_0, L )
    pot_energy[t] = sum(potential)
    kin_energy[t],total_velocity[t] = store_quantities(N,velocity)
    ## Dynamic plotting
    # time[t] = t 
    # pos_time[t] = pos[0,1]
    # plt.xlim([0,L])
    # plt.ylim([0,L])
    # plt.show()
    # ax = Axes3D(fig)                            # Define axis
    # ax.scatter(pos[:,0], pos[:,1], pos[:,2])    # Plot positions#
    ## Print
    print velocity[1,2]
    # print pos[1,2]
    ## Write to output file
    out_vel = str(velocity[1,2]) + "\n"
    with open("output.dat", "a") as fh:
        fh.write(out_vel)
fh.close() # Close output file

## Plotting
# total_energy = np.add(kin_energy,pot_energy)
# print kin_energy
# plt.plot(time,pot_energy, 'r')
# plt.show()
# plt.plot(time,kin_energy, 'b')
# plt.show()
# plt.plot(time,total_energy, 'g')
# plt.show()
# plt.plot(time,pot_energy,'g')