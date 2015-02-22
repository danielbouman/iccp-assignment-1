import numpy as np
from normalize_momentum import normalize_momentum
def initvelocity( N, T,m):
	velocity = np.zeros((N,3),dtype=float) #Initialize velocity array
	kb = 0.1
	# Assign random uniform velocity
	for ii in xrange(0,N-1):
		velocity[ii,0] = np.sqrt(-(kb*T)*np.log(np.random.random()))
		velocity[ii,1] = np.sqrt(-(kb*T)*np.log(np.random.random()))
		velocity[ii,2] = np.sqrt(-(kb*T)*np.log(np.random.random()))

		velocity = normalize_momentum(N, velocity)
	return velocity;