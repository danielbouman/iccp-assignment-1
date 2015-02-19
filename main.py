import numpy as np
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold='nan')

L = 1 # box length
M = 3 # unit cells per dimension
N = 4*np.power(M,3) #Number of particles, 4 per unit cell

##Initialization of particles
#Homogeneous distribution

from initpos_function import initpos

pos = initpos( L,N,M )

fig = pylab.figure()
ax = Axes3D(fig)

ax.scatter(pos[:,0], pos[:,1], pos[:,2])
plt.show()