## Import libraries
import numpy as np
## Import functions
from distance import pair_distance 
def acceleration(N,pos,L):
	## Variables
	acceleration = np.zeros((N, 3),dtype=float)
	potential = np.zeros((N, 1),dtype=float)
	distance = np.zeros((3),dtype=float)
	m = 1
#	sigma = 1
	epsilon = 1.65*np.power(10,-21)
	epsilon = 1
	cutoff = L*2
	for ii in xrange(0, N-1):
		for iii in xrange(0, N-1):
			if ii != iii:
				distance[0] = pair_distance(pos[ii,0],pos[iii,0],L) 	# x direction
				distance[1] = pair_distance(pos[ii,1],pos[iii,1],L) 	# y direction
				distance[2] = pair_distance(pos[ii,2],pos[iii,2],L) 	# z direction
				abs_distance = np.sqrt(np.power(distance[0],2)+np.power(distance[1],2)+np.power(distance[2],2))
				if abs_distance < cutoff:
				# F = (12*(np.power(sigma,12))/(np.power(total_distance,13)))-6*((np.power(sigma,6))/(np.power(total_distance,7)))
					V = 4*epsilon*(np.power(abs_distance,-12)-np.power(abs_distance,-6))
					F = -epsilon*(48*np.power(abs_distance,-13)-24*np.power(abs_distance,-7))
				else:
					F = 0
				acceleration[ii,0] = (F/m)*(distance[0]/abs_distance)+acceleration[ii,0]
				acceleration[ii,1] = (F/m)*(distance[1]/abs_distance)+acceleration[ii,1]
				acceleration[ii,2] = (F/m)*(distance[2]/abs_distance)+acceleration[ii,2]
				potential[ii] = V + potential[ii]+V

	return acceleration,potential;