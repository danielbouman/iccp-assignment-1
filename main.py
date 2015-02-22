## Import libraries
import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold='nan')

## Import functions
from initpos_function import initpos
from initvelocity import initvelocity
from velocity_verlet import velocity_verlet
from normalize_momentum import normalize_momentum
from store_quantities import store_quantities

## Assign variables
L = 70                                # Box length
M = 2                                   # Unit cells per dimension
N = 4*np.power(M,3)                     # Number of particles, 4 per unit cell
h = 0.0004 								# timestep
T = 200
m = 1

## Init particle position, homogeneous distribution
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
for t in xrange(0, 100):
	pos,velocity,a_0,potential = velocity_verlet( N, h, pos, velocity, a_0, L )
	pot_energy[t] = sum(potential)
	vel_time[t] = velocity[0,1]
	time[t] = t
	pos_time[t] = pos[0,1]
	kin_energy[t],total_velocity[t] = store_quantities(N,velocity)
	#if np.mod(t,10) == 0:
	#	velocity = normalize_momentum(N, velocity)


total_energy = np.add(kin_energy,pot_energy)
#print kin_energy
plt.plot(time,total_energy, 'r')
#plt.plot(time,pot_energy,'g')

plt.show()


	#print velocity[1,2]
	# print pos[1,2]
	# fig = pylab.figure()          	          # Define figure
	# ax = Axes3D(fig)                        # Define axis
	# ax.scatter(pos[:,0], pos[:,1], pos[:,2])# Plot positions#
	# pylab.xlim([0,L])
	# pylab.ylim([0,L])
	# plt.show()