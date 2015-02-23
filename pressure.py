## Import libraries
import numpy as np
## Define function
def virial_pressure(beta,N,r,F):
    n = 1
    pressure = np.zeros((N,3),dtype=float)
    for ii in xrange(0,N-1):
        pressure[ii,0] = n/beta - n/(3*N)*(-F*r[ii,0]);     # x dimension
        pressure[ii,1] = n/beta - n/(3*N)*(-F*r[ii,1]);     # y dimension
        pressure[ii,2] = n/beta - n/(3*N)*(-F*r[ii,2]);     # z dimension

    pressure = np.add
    return pressure;