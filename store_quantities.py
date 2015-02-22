import numpy as np
# Import functions
def store_quantities(N,velocity):
	kinetic_energy = 0.5*sum(sum(np.array(velocity)**2))

	return kinetic_energy;