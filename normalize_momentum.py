## Import libraries
import numpy as np
## Define function
def normalize_momentum(N,velocity,T):
	kb = 1.38*np.power(10,-23)
	## Normalize velocities
	total_velocity_x = sum(velocity[:,0])
	total_velocity_y = sum(velocity[:,1])
	total_velocity_z = sum(velocity[:,2])
	velocity[:,0] = velocity[:,0]-total_velocity_x/N
	velocity[:,1] = velocity[:,1]-total_velocity_y/N
	velocity[:,2] = velocity[:,2]-total_velocity_z/N

	rescaling_factor = np.sqrt((3*(N-1)*kb*T)/(sum(sum(np.array(velocity)**2))))

	velocity = rescaling_factor*velocity

	return velocity;