"""
acceleration calculates the total force per particle. From this it calculates the total acceleration components of each particle.
The virial (which is needed for the pressure), the potential energy (needed for the total energy) and amount of particles per distance
(needed for the correlation length) is calculated in this function.
N           : amount of particles
pos 		: position of all the particles
L           : length of box
hist_bins   : The 'bins' where we divide our distances in to calculate the correlation function
"""

## Import libraries
import numpy as np
## Import functions
from distance import pair_distance 
def acceleration(N,pos,L,cutoff, hist_bins):
	## Reset variables
	acceleration = np.zeros((N, 3),dtype=float)
	potential = np.zeros((N, 1),dtype=float)
	distance = np.zeros((3),dtype=float)
	dist_list = np.zeros((N,N),dtype=float)
	virial = 0

	for ii in range(0, N):								# Loop over each particle
		for iii in range(0, N):						# Loop over all other particles
			if ii != iii:								# Exclude same particles
				distance[0] = pair_distance(pos[ii,0],pos[iii,0],L) 	# x distance
				distance[1] = pair_distance(pos[ii,1],pos[iii,1],L) 	# y distance
				distance[2] = pair_distance(pos[ii,2],pos[iii,2],L) 	# z distance
				abs_distance = np.sqrt(np.power(distance[0],2)+np.power(distance[1],2)+np.power(distance[2],2)) # Total distance
				dist_list[ii,iii] = abs_distance																# Save distance for correlation length calc

				if abs_distance < cutoff:																		# Set forces to zero if the distance is greater than the cutoff
					V = 4*(np.power(abs_distance,-12)-np.power(abs_distance,-6))			# Calculate lennard jones potential
					F = (48*np.power(abs_distance,-13)-24*np.power(abs_distance,-7))
				else:
					F = 0
					V = 0

				virial= abs_distance*F*0.5+virial										# Virial is the distance between two particles times the force between them, divide by 2 to avoid double counting
				acceleration[ii,0] = -F*(distance[0]/abs_distance)+acceleration[ii,0]	# Multiply the abs force with each component of the distance between two particles
				acceleration[ii,1] = -F*(distance[1]/abs_distance)+acceleration[ii,1]
				acceleration[ii,2] = -F*(distance[2]/abs_distance)+acceleration[ii,2]
				potential[ii] = V + potential[ii]

	dist_list = dist_list.flatten()							# Change the 2d array to a 1d array
	dist_list = dist_list[dist_list !=0]					# remove zeroes from the 1d array
	dist_hist,_ = np.histogram(dist_list,bins=hist_bins)	# histogram of distances, with width delta r.
	return acceleration,potential,virial,dist_hist;