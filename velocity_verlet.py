# Import libraries
import numpy as np
# Import functions
from acceleration import acceleration
# Define velocity verlet function
def velocity_verlet(L,D,N,h,pos,a_0):
    v_half_h = pos + 0.5*a_0*h
    pos_h = pos + v_half_h*h
    a_h = acceleration(pos_h)
    v_h = v_half_h+0.5*a_h*h
    a_0 = a_h
    pos = pos_h