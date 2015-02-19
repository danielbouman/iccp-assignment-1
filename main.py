## Import libraries
import numpy as np
#np.set_printoptions(threshold='nan')

## Assign variables
L = 1                                   # box length
M = 3                                   # unit cells per dimension
N = 4*np.power(M,3)                     #Number of particles, 4 per unit cell

## Initialization of particles, homogeneous distribution
from initpos_function import initpos
pos = initpos( L,N,M )

## Plot particles
from scatterplot_function import scat_plot
scat_plot(pos[:,0],pos[:,1],pos[:,2])