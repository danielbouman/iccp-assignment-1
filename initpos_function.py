import numpy as np
def initpos(L, N, M):
	# Given length of a box of D dimensions, distribute N particles homogeneous across
	pos = np.zeros((N, 3),dtype=float) #Initialize position array
	a = float(L)/M #Lattice constant
	j = 0 #counter that runs over all particles
	for ii in xrange(0, M): # loop through unit cells in the x-direction
		for iii in xrange(0, M): # loop through unit cells in the y-direction
			for iiii in xrange(0, M): # loop through unit cells in the z-direction
				pos[j,0] = a*ii 		# the first particle in each unit cell is added by adding the vector distance to the position of the unit cell
				pos[j,1] = a*iii 		# y position of the first particle
				pos[j,2] = a*iiii		# z position of the first particle
				j = j + 1 				# Move to next particle
				pos[j,0] = a*ii 		# Now the same for the second particle at a different position
				pos[j,1] = a*iii+0.5*a 	# y position of the second particle
				pos[j,2] = a*iiii+0.5*a # z position of the second particle
				j = j + 1 				# Move to next particle
				pos[j,0] = a*ii+0.5*a 	# Now the same for the third particle at a different position
				pos[j,1] = a*iii 		# y position of the third particle
				pos[j,2] = a*iiii+0.5*a # z position of the third particle
				j = j + 1 				# Move to next particle
				pos[j,0] = a*ii+0.5*a 	# Now the same for the fourth particle at a different position
				pos[j,1] = a*iii+0.5*a 	# y position of the fourth particle
				pos[j,2] = a*iiii 		# z position of the fourth particle
				j = j + 1 				# Move to next particle
			#end for loop
		#end for loop
	#end for loop
	return pos;