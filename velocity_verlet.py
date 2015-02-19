# Import libraries
import numpy as np
# Import functions
from acceleration import acceleration
# Define velocity verlet function
def velocity_verlet(N, h, pos, a_0, L):
    v_half_h = np.add(pos,0.5*a_0*h)
    pos_h = np.add(pos,v_half_h*h)
    if np.less(pos_h,0): # periodic boundary condition
        pos_h = L - np.fabs(pos_h)

    a_h = acceleration(N, pos_h, L)
    v_h = np.add(v_half_h,0.5*a_h*h)
    a_0 = a_h
    pos = pos_h
    if np.less(pos,0): # periodic boundary condition
        pos = L - np.fabs(pos_h)

    return pos;