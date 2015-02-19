import numpy as np
def initvelocity( N ):
	velocity = np.zeros((N,3),dtype=float) #Initialize velocity array
	
	# Assign random uniform velocity
	for ii in xrange(0,N-1):
		velocity[ii,0] = 100*np.sqrt(-2*np.log(np.random.random()))
		velocity[ii,1] = 100*np.sqrt(-2*np.log(np.random.random()))
		velocity[ii,2] = 100*np.sqrt(-2*np.log(np.random.random()))

	return velocity;