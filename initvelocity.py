def initvelocity(L,D,N):

	velocity = np.zeros((N,3),dtype=float) #Initialize velocity array
	
	# Assign random uniform velocity
	for ii in xrange(0,N):
			velocity[ii][1] = random.uniform(-5,5) #velocity is assigned uniformly between -5 and 5, this should be changed to boltzmann distribution!
			velocity[ii][2] = random.uniform(-5,5)
			velocity[ii][3] = random.uniform(-5,5)
			
return;