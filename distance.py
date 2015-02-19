def distance(Position1,Position2):
		distance_x = (Position2[0]-Position1[0]) #Distance in the x-dimension between position 1 and 2. Does not yet take into account periodic boundary conditions
		if np.fabs(distance_x)>(L/2):			#
			distance_x = distance_x - 2*np.fmod(distance_x,(L/2))

		distance_y = (Position2[1]-Position1[1])
		if np.fabs(distance_y)>(L/2):
			distance_y = distance_y - 2*np.fmod(distance_y,(L/2))

		distance_z = (Position2[2]-Position1[2])
		if np.fabs(distance_z)>(L/2):
			distance_z = distance_z - 2*np.fmod(distance_z,(L/2))

		distance = np.sqrt(np.power(distance_x,2)+np.power(distance_y,2)+np.power(distance_z,2))