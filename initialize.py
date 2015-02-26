"""
Initialize the particle position and momentum.
momentum
N   : number of particles
T   : desired temperature
position
L   : vertex length of volume V
N   : total number of particles
M   : number of unit cells per dimension
"""
## Import functions
import numpy as np
from normalize_momentum import normalize_momentum

## Initial momentum function
def momentum(N,T):
	init_momentum = np.zeros((N,3),dtype=float)
	## Assign velocity from uniform random number
	for ii in xrange(0,N):
		init_momentum[ii,0] = np.sqrt(-2*np.log(np.random.random()))
		init_momentum[ii,1] = np.sqrt(-2*np.log(np.random.random()))
		init_momentum[ii,2] = np.sqrt(-2*np.log(np.random.random()))
	init_momentum = normalize_momentum(N,init_momentum,T)
	return init_momentum;
	
## Initial position position
def position(L, N, M):
    ## Distribute N particles using fcc lattice over M*L cubic box 
    pos = np.zeros((N, 3),dtype=float)  # Init position array
    a = float(L)/M                      # Lattice constant
    j = 0                               # Set counter over all particles
    for ii in xrange(0, M):             # Unit cells, x-direction
        for iii in xrange(0, M):        # Unit cells, y-direction
            for iiii in xrange(0, M):   # Unit cells, z-direction
                ## Corner particle in unit cell
                pos[j,0] = a*ii         # x-position
                pos[j,1] = a*iii        # y-position
                pos[j,2] = a*iiii       # z-position
                j = j + 1               # Move to next particle
                ## First center particle in unit cell
                pos[j,0] = a*ii         
                pos[j,1] = a*iii+0.5*a   
                pos[j,2] = a*iiii+0.5*a  
                j = j + 1                
                ## Second center particle in unit cell
                pos[j,0] = a*ii+0.5*a    
                pos[j,1] = a*iii         
                pos[j,2] = a*iiii+0.5*a  
                j = j + 1                
                ## Third center particle in unit cell
                pos[j,0] = a*ii+0.5*a    
                pos[j,1] = a*iii+0.5*a  
                pos[j,2] = a*iiii       
                j = j + 1
    pos = np.add(a*0.05,pos)
    return pos;