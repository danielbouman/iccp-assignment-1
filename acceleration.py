## Import libraries
import numpy as np
## Import functions
from distance import pair_distance 
def acceleration(N,pos,L):
	acceleration = np.zeros((N, 3),dtype=float)
	m = 0.00001
	sigma = 00.000001
	epsilon = 0.00001
	for ii in xrange(0, N-1):
		for iii in xrange(0, N-1):
			if ii != iii:
				x_distance = pair_distance(pos[ii,0],pos[iii,0],L)
				y_distance = pair_distance(pos[ii,1],pos[iii,1],L)
				z_distance = pair_distance(pos[ii,2],pos[iii,2],L)
				total_distance = np.sqrt(np.power(x_distance,2)+np.power(y_distance,2)+np.power(z_distance,2))
				F = (12*(np.power(sigma,12))/(np.power(total_distance,13)))-6*((np.power(sigma,6))/(np.power(total_distance,7)))
				print F
				acceleration[ii,0] = (F/m)*(x_distance/total_distance)+acceleration[ii,0]
				acceleration[ii,1] = (F/m)*(y_distance/total_distance)+acceleration[ii,1]
				acceleration[ii,2] = (F/m)*(z_distance/total_distance)+acceleration[ii,2]

	return acceleration;