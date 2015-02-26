"""
Determine physical quantities after equilibiration phase.
pressure calculates the pressure by a virial expansion. The third term is to correct for the cutoff length
pressure:
T           : current temperature
N           : amount of particles
L           : length of box
virial      : sum of the virial between every particle
r_c         : cutoff length

----
specific_heat calculates the specific heat by Lebowitz' formula.
N           : amount of particles
T           : current temperature
K           : total kinetic energy over a predefined amount of timesteps
"""
## Import libraries
import numpy as np
## Define function
def pressure(T,N,L,virial,r_c):
	virial_pressure = np.zeros((N,3),dtype=float)
	V = np.power(L,3)                                              # Calculate volume from box length L
	virial_pressure = (float(N)/V)*T + 1/(3*float(V))*virial-(2*np.pi*np.power(N,2))\
		/(3*np.power(V,2))*(((48/9)*np.power(r_c,-9))-((24/3)*np.power(r_c,-3)))      # Formula given in the book for the pressure. g(r) = 1
	return virial_pressure;
	
# Define velocity verlet function
def specific_heat(N,T,E,K):
    inverse_sh2 = (2/float(3*N) )-( np.var(K) )/( np.power(K[-1],2 )) # inverse of the specific heat by Lebowitz' formula
    sh2 = np.power(inverse_sh2,-1)/n                                  # specific heat per particle
    return sh1,sh2;