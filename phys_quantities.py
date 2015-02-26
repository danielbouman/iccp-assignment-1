"""
Determine physical quantities after equilibiration phase.
"""
## Import libraries
import numpy as np
## Define function
def pressure(T,N,L,virial,r_c):
	virial_pressure = np.zeros((N,3),dtype=float)
	V = np.power(L,3)
	virial_pressure = (float(N)/V)*T + 1/(3*float(V))*virial-(2*np.pi*np.power(N,2))\
		/(3*np.power(V,2))*(((48/9)*np.power(r_c,-9))-((24/3)*np.power(r_c,-3)))
	return virial_pressure;
	
# Define velocity verlet function
def specific_heat(N,T,E,K):
	sh1 = 1/(np.power(T,2) )*np.var(E)
    inverse_sh2 =  ((2/(3*N) )-( np.var(np.power(K,2)) )/( np.power(K[-1],2 )) #inverse of the specific heat by Lebowitz' formula
	sh2 = np.power(inverse_sh2,-1)
	return sh1,sh2;