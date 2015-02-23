import numpy as np
# Import functions
def store_quantities(N,velocity):
	kinetic_energy = sum(sum(0.5*(np.power(velocity,2))))
	# print kinetic_energy
	total_velocity = sum(sum(np.array(velocity)))
	return (total_velocity, kinetic_energy)