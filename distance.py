def distance(Position1,Position2):
		distance_x = (Position2[1]-Position1[1])
		if math.fabs(distance_x)>(L/2):
			distance_x = distance_x - 2*math.fmod(distance_x,(L/2))

		distance_y = (Position2[2]-Position1[2])
		if math.fabs(distance_y)>(L/2):
			distance_y = distance_y - 2*math.fmod(distance_y,(L/2))

		distance_z = (Position2[3]-Position1[3])
		if math.fabs(distance_z)>(L/2):
			distance_z = distance_z - 2*math.fmod(distance_z,(L/2))

		distance = math.sqrt(math.pow(distance_x,2)+math.pow(distance_y,2)+math.pow(distance_z,2))