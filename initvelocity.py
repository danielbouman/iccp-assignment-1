def initvelocity(L,D,N):

	# Create a variable-sized 2d list
	rows = N
	cols = D
	velocity=[]
	for row in xrange(rows): velocity += [[0]*cols] 

	# Assign random uniform velocity
	for ii in xrange(0,rows-1):
		for iii in xrange(0,cols-1):
			velocity[ii][iii] = random.uniform(0.2,5)
			

return;