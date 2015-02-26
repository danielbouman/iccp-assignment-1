# Import libraries
import numpy as np
import save_data as save
# Import functions
#
def save_phys(data,name,first=False):
    data_variance = np.var(data)
    data_mean = np.mean(data)
    data_array = name+"\t"+str(data_mean)+"\t"+str(data_variance)
    if first:
        header_text = "Quantity\tmean\t\t\tvariance"
        write_mode = "w"
    else:
        header_text = ""
        write_mode = "a"
    save.save(data_array,"phys_quantities",header_text,write_mode)
    return