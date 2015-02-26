"""
Normalize and rescale particle momentum so they correspond with the desired temperature. This is done by comparing the
current total kinetic energy and the total kinetic energy that is expected with the desired temperature and
the equipartition theorem.
normalize_momentum(N,momentum,T,E_k=-1)
N           : number of particles
momentum    : particle momentum
T           : desired temperature
E_k         : total kinetic energy
"""
## Import libraries
import numpy as np
## Define function
def normalize_momentum(N,momentum,T,E_k=-1):
    total_momentum = np.zeros(momentum.shape,dtype=float)
    ## Normalize velocities
    total_momentum[:,0] = sum(momentum[:,0])                    # total momentum in the x direction
    total_momentum[:,1] = sum(momentum[:,1])                    # total momentum in the y direction
    total_momentum[:,2] = sum(momentum[:,2])                    # total momentum in the z direction
    momentum[:,0] = momentum[:,0]-total_momentum[:,0]/N         # readjust momentum per particle in the x direction
    momentum[:,1] = momentum[:,1]-total_momentum[:,1]/N         # readjust momentum per particle in the y direction
    momentum[:,2] = momentum[:,2]-total_momentum[:,2]/N         # readjust momentum per particle in the z direction

    ## Determine rescaling factor
    if E_k == -1:       # if no total kinetic energy is given
        rescaling_factor = np.sqrt((3*(N-1)*T)/(sum(sum(np.array(momentum)**2))))
    else:               # if total kinetic energy is already determined
        rescaling_factor = np.sqrt((3*(N-1)*T)/(2*E_k))
    momentum = rescaling_factor*momentum

    return momentum;