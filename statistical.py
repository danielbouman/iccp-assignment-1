# Import libraries
import numpy as np
import save
# Import functions
#
def save_phys(data,name):
    data_variance = np.var(data)
    data_mean = np.mean(data)
    data_array = name 
    save.save(data_array,"phys_quantities",header)
    return