def initpos(L,N,M):
	# Given length of a box of D dimensions, distribute N particles homogeneous across

	pos = np.zeros((N,3),dtype=float) #Initialize position array
	a = L/M #Lattice constant

	j = 0 #counter that runs over all particles

	for ii in xrange(0,M-1): # loop through unit cells in the x-direction
		for iii in xrange(0,M-1): # loop through unit cells in the y-direction
			for iiii in xrange(0,M-1): # loop through unit cells in the z-direction
				cell_pos = a(ii,iii,iiii) #position of the lower left corner at the back of each unit cell.

				pos(j,1) = a*ii+0.5*a #the first particle in each unit cell is added by adding the vector distance to the position of the unit cell
				pos(j,2) = a*ii 	  # y position of the first particle
				pos(j,3) = a*ii+0.5*a # z position of the first particle
				j = j + 1 # Move to next particle

				pos(j,1) = a*ii # Now the same for the second particle at a different position
				pos(j,2) = a*ii+0.5*a 	# y position of the second particle
				pos(j,3) = a*ii+0.5*a 	# z position of the second particle
				j = j + 1 # Move to next particle
	

	return;