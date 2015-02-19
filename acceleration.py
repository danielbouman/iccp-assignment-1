import numpy as np
def acceleration(pos,m):
	acceleration = np.zeros((N, 3),dtype=float)
	for ii in xrange(0, N-1):
		for iii in xrange(0, N-1):
			x_distance = distance(pos[ii,0],pos[iii,0])
			y_distance = distance(pos[ii,1],pos[iii,1])
			z_distance = distance(pos[ii,2],pos[iii,2])
			F_x = ((np.power(sigma,12))/(np.power(x_distance,13)))-((np.power(sigma,6))/(np.power(x_distance,7)))
			F_y = ((np.power(sigma,12))/(np.power(y_distance,13)))-((np.power(sigma,6))/(np.power(y_distance,7)))
			F_z = ((np.power(sigma,12))/(np.power(z_distance,13)))-((np.power(sigma,6))/(np.power(z_distance,7)))
			acceleration[ii,0] = F_x/m
			acceleration[ii,1] = F_y/m
			acceleration[ii,2] = F_z/m
    return #moet hier niet nog een punt komma achter¿