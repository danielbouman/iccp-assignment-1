## Import libraries
import numpy as np
"""
diffusion_constant calculates the diffusion_constant per time step. The displacement is first calculated in the x,y,z direction,
then averaged per particle, from which the average total displacement squared is calculated. Dividing by the time step will give an estimate for D
in reduced units.
"""

def diffusion_constant(displacement_xyz,h,L):
    avg_displacement_squared_xyz = np.average(np.sum(np.power(displacement_xyz,2),axis=0))# Calculate the average displacement squared in x,y,z direction
    avg_displacement_squared = np.sum(avg_displacement_squared_xyz) # Summing the average displacement squared in each direction gives us the average value of the total displacement

    D = avg_displacement_squared/float(h) # Formula for diffusive behaviour
    return D;