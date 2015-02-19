# Import libraries
import numpy as np
# Import functions
from acceleration import acceleration
# Define velocity verlet function
def velocity_verlet(N, h, pos, a_0, L):
    v_half_h = np.add(pos,0.5*a_0*h)
    pos_h = np.add(pos,v_half_h*h)
    pos_h = np.where(pos_h<0,L-np.fabs(pos_h)) # periodic boundary condition
    a_h = acceleration(N, pos_h, L)
    v_h = np.add(v_half_h,0.5*a_h*h)
    a_0 = a_h
    pos = pos_h
    pos = np.where(pos<0,L-np.fabs(pos)) # periodic boundary condition
    return pos;