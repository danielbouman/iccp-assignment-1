"""
Normalize and rescale particle momentum.
normalize_momentum(N,momentum,T,E_k=-1)
N           : number of particles
momentum    : particle momentum
T           : desired temperature
E_k         : total kinetic
"""
## Import libraries
import numpy as np
## Define function
def normalize_momentum(N,momentum,T,E_k=-1):
    total_momentum = np.zeros(momentum.shape,dtype=float)
    ## Normalize velocities
    total_momentum[:,0] = sum(momentum[:,0])
    total_momentum[:,1] = sum(momentum[:,1])
    total_momentum[:,2] = sum(momentum[:,2])
    momentum[:,0] = momentum[:,0]-total_momentum[:,0]/N
    momentum[:,1] = momentum[:,1]-total_momentum[:,1]/N
    momentum[:,2] = momentum[:,2]-total_momentum[:,2]/N
    ## Determine rescaling factor
    if E_k == -1:       # if no total kinetic energy is given
        rescaling_factor = np.sqrt((3*(N-1)*T)/(sum(sum(np.array(momentum)**2))))
    else:               # if total kinetic energy is already determined
        rescaling_factor = np.sqrt((3*(N-1)*T)/(2*E_k))
    momentum = rescaling_factor*momentum

    return momentum;