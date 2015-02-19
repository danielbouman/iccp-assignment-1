import numpy as np
def initvelocity(L,D,N):
	velocity = np.zeros((N,3),dtype=float) #Initialize velocity array
	
	# Assign random uniform velocity
	for ii in xrange(0,N-1):
			velocity[ii][0] = np.sqrt(-2*log(random.random())
			velocity[ii][1] = np.sqrt(-2*log(random.random())
			velocity[ii][2] = np.sqrt(-2*log(random.random())
			
return;