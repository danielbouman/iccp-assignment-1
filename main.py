import numpy as np
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D


L = 1 #Length of box
M = 10 #M is the amount of unit cells per dimension
N = 4*np.power(M,3) #Number of particles. The factor 4 is for the fact that we have 4 particles per unit cell

##Initialization of particles
#Homogeneous distribution
