import numpy as np
def initvelocity( N ):
	velocity = np.zeros((N,3),dtype=float) #Initialize velocity array
	
	# Assign random uniform velocity
	for ii in xrange(0,N-1):
		velocity[ii,0] = np.sqrt(-2*np.log(np.random.random()))
		velocity[ii,1] = np.sqrt(-2*np.log(np.random.random()))
		velocity[ii,2] = 10*np.sqrt(-2*np.log(np.random.random()))
		# velocity[ii,0] = 0
		# velocity[ii,1] = 0
		# velocity[ii,2] = 0

	return velocity;