import numpy as np
# Import functions
def store_quantities(N,velocity):
	kinetic_energy = 0.5*(np.power(velocity,2))
	total_velocity = sum(sum(np.array(velocity)))
	return kinetic_energy,total_velocity;