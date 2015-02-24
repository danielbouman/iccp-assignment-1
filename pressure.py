## Import libraries
import numpy as np
## Define function
def virial_pressure(T,N,L,virial,r_c):
    pressure = np.zeros((N,3),dtype=float)
    kb = 1.1
    V = np.power(L,3)
    pressure = float((N/V)*kb*T - 1/(3*V)*virial-(2*np.pi*np.power(N,2))/(3*np.power(V,2))*(((48/11)*np.power(r_c,-11))-((24/5)*np.power(r_c,-5))))
    return pressure;