"""
The distance function returns the effective x,y, or z component. The effective distance is needed because the simulation used
periodic boundary conditions. 
Position1 			: position of the first particle
Position2 			: position of the second particle
L 					: length of the box
"""

import numpy as np
def pair_distance(Position1,Position2,L):
	distance = Position2-Position1 	#Distance in the x-dimension between position 1 and 2. Does not yet take into account periodic boundary conditions
	if np.fabs(distance)>(L/2):		# Check if there is a shorter distance with periodic boundary conditions
		if distance>0:				# Check for the sign of the distance
			distance = distance - L # and compensate accordingly
		else:
			distance = distance + L
	return distance;