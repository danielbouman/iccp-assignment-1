## Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold='nan')

## Assign variables
L = 1                                   # Box length
M = 3                                   # Unit cells per dimension
N = 4*np.power(M,3)                     # Number of particles, 4 per unit cell

## Initialization of particles, homogeneous distribution
from initpos_function import initpos
pos = initpos( L,N,M )

## Plot particles
fig = pylab.figure()                    # Define figure
ax = Axes3D(fig)                        # Define axis

ax.scatter(pos[:,0], pos[:,1], pos[:,2])# Plot positions
plt.show()                              # Display plot