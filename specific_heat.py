# Import libraries
import numpy as np
# Define velocity verlet function
def specific_heat(N,T,E,K):
	sh1 = 1/(np.power(T,2) )*np.var(E)
	sh2 = np.power( ((2/(3*N) )-( np.var(K) )/( K[-1] )),-1 )
	return sh1,sh2;
