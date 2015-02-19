## Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold='nan')

## Assign variables
L = 100                                   # Box length
M = 2                                   # Unit cells per dimension
N = 4*np.power(M,3)                     # Number of particles, 4 per unit cell
h = 0.04 #timestep

## Init particle position, homogeneous distribution
from initpos_function import initpos
pos = initpos( L,N,M )

## Init velocity
from initvelocity import initvelocity
velocity = initvelocity( N )

## Init acceleration
a_0 = np.zeros((N,3),dtype=float) #Initialize acceleration array




## Velocity verlet
from velocity_verlet import velocity_verlet

for t in xrange(0, 100):
	pos_2 = velocity_verlet( N, h, pos, a_0, L )
	fig = pylab.figure()          	          # Define figure
	ax = Axes3D(fig)                        # Define axis
	ax.scatter(pos_2[:,0], pos_2[:,1], pos_2[:,2])# Plot positions#
	pylab.xlim([0,L])
	pylab.ylim([0,L])
	plt.show()     