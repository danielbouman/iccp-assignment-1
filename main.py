## Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold='nan')

## Assign variables
L = 1                                   # Box length
M = 2                                   # Unit cells per dimension
N = 4*np.power(M,3)                     # Number of particles, 4 per unit cell
h = 1.01 #timestep

## Init particle position, homogeneous distribution
from initpos_function import initpos
pos = initpos( L,N,M )
print pos

## Init velocity
from initvelocity import initvelocity
velocity = initvelocity( N )

## Init acceleration
a_0 = np.zeros((N,3),dtype=float) #Initialize acceleration array


## Plot particles
fig = pylab.figure()                    # Define figure
ax = Axes3D(fig)                        # Define axis

ax.scatter(pos[:,0], pos[:,1], pos[:,2])# Plot positions

pylab.xlim([0,L])
pylab.ylim([0,L])
plt.show()                              # Display plot

## Velocity verlet
from velocity_verlet import velocity_verlet

for t in xrange(0, 100):
	pos_2 = velocity_verlet( N, h, pos, a_0, L )
	#print pos_2
	#print pos
	## Plot particles
	#pos_3 = np.subtract(pos_2,pos)
	#print pos_3
	# pos = np.subtract(pos_2,pos)
	fig = pylab.figure()          	          # Define figure
	ax = Axes3D(fig)                        # Define axis
	ax.scatter(pos_2[:,0], pos_2[:,1], pos_2[:,2])# Plot positions#
	pylab.xlim([0,L])
	pylab.ylim([0,L])
	plt.show()                              # Display plot

