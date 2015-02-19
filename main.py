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


## Plot particles
#fig = pylab.figure()                    # Define figure
#ax = Axes3D(fig)                        # Define axis

#ax.scatter(pos[:,0], pos[:,1], pos[:,2])# Plot positions
#plt.
#pylab.xlim([0,L])
#pylab.ylim([0,L])
#plt.ion()
#plt.show()                              # Display plot


## Velocity verlet
from velocity_verlet import velocity_verlet

fig = pylab.figure()          	          # Define figure
ax = Axes3D(fig)                        # Define axis
for t in xrange(0, 100):
	pos = velocity_verlet( N, h, pos, a_0, L )
	#print pos_2	
	#print pos
	## Plot particles
	#pos_3 = np.subtract(pos_2,pos)
	#print pos_3
	# pos = np.subtract(pos_2,pos)
	#ax.clear()
	#ax.scatter(pos[:,0], pos[:,1], pos[:,2])# Plot positions#
	#pylab.xlim([0,L])
	#pylab.ylim([0,L])
	#plt.show()
	#time.sleep(0.5)

fig = pylab.figure()                    # Define figure
ax = Axes3D(fig)                        # Define axis

ax.scatter(pos[:,0], pos[:,1], pos[:,2])# Plot positions
#plt.
pylab.xlim([0,L])
pylab.ylim([0,L])
plt.ion()
plt.show()                              # Display plot


