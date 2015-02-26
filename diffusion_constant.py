## Import libraries
import numpy as np
## Import functions
def diffusion_constant(pos_h,pos,h,L):
    displacement_xyz = np.absolute(np.subtract(pos_h,pos)) # Diplacement in x,y,z direction for each particle
    displacement_xyz = np.where(displacement_xyz>(L/2), np.absolute(displacement_xyz-L), pos) # Calculate absolute shift in x,y,z with periodic boundary conditions
    avg_displacement_squared_xyz = np.average(np.sum(np.power(displacement_xyz,2),axis=0))# Calculate the average displacement squared in x,y,z direction
    avg_displacement_squared = np.sum(avg_displacement_squared_xyz) # Summing the average displacement squared in each direction gives us the average value of the total displacement
    D = avg_displacement_squared/float(h) # Formula for diffusive behaviour
    return D;