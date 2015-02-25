## Import libraries
import numpy as np
## Import functions
from distance import pair_distance 
def acceleration(N,pos,L,cutoff, hist_bins):
	## Variables
	acceleration = np.zeros((N, 3),dtype=float)
	potential = np.zeros((N, 1),dtype=float)
	distance = np.zeros((3),dtype=float)
	dist_list = np.zeros((N,N),dtype=float)
	virial = 0
#	sigma = 1
#	epsilon = 1.65*np.power(10,-21)
	for ii in xrange(0, N):
		for iii in xrange(0, N):
			if ii != iii:
				distance[0] = pair_distance(pos[ii,0],pos[iii,0],L) 	# x direction
				distance[1] = pair_distance(pos[ii,1],pos[iii,1],L) 	# y direction
				distance[2] = pair_distance(pos[ii,2],pos[iii,2],L) 	# z direction
				abs_distance = np.sqrt(np.power(distance[0],2)+np.power(distance[1],2)+np.power(distance[2],2))
				dist_list[ii,iii] = abs_distance

				if abs_distance < cutoff:
					V = 4*(np.power(abs_distance,-12)-np.power(abs_distance,-6))
					F = (48*np.power(abs_distance,-13)-24*np.power(abs_distance,-7))
				else:
					F = 0
					V = 0
				virial= abs_distance*F+virial
				acceleration[ii,0] = -F*(distance[0]/abs_distance)+acceleration[ii,0]
				acceleration[ii,1] = -F*(distance[1]/abs_distance)+acceleration[ii,1]
				acceleration[ii,2] = -F*(distance[2]/abs_distance)+acceleration[ii,2]
				potential[ii] = V + potential[ii]

	dist_list = dist_list.flatten()										# Change the 2d array to a 1d array
	dist_list = dist_list[dist_list !=0]								# remove zeroes from the 1d array
	dist_hist,_ = np.histogram(dist_list,bins=hist_bins)				# histogram of distances, with width delta r
	return acceleration,potential,virial,dist_hist;