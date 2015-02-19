# Import libraries
import numpy as np
# Import functions
from acceleration import acceleration
# Define velocity verlet function
def velocity_verlet(L,D,N,h,pos,a_0):
    v_half_h = map(add,pos,0.5*a_0*h)
    pos_h = map(add,pos,v_half_h*h)
    a_h = acceleration(pos_h)
    v_h = map(add, v_half_h,0.5*a_h*h)
    a_0 = a_h
    pos = pos_h