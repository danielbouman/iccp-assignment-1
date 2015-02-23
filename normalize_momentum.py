## Import libraries
import numpy as np
## Define function
def normalize_momentum(N,velocity):
	## Normalize velocities
	total_velocity_x = sum(velocity[:,0])
	total_velocity_y = sum(velocity[:,1])
	total_velocity_z = sum(velocity[:,2])
	velocity[:,0] = velocity[:,0]-total_velocity_x/N
	velocity[:,1] = velocity[:,1]-total_velocity_y/N
	velocity[:,2] = velocity[:,2]-total_velocity_z/N

	return velocity;