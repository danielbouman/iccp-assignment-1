# Import libraries
import numpy as np
import save_data as save
# Import functions
#
def save_phys(data,name,first=False,others=""):
    data_variance = np.var(data)
    data_mean = np.mean(data)
    data_array = name+"\t"+str(data_mean)+"\t"+str(data_variance)
    if first:
        header_text = others+"\n===========================================\
        \nQuantity:\tMean:\t\t\tVariance:\t\
        \n-------------------------------------------\n"
        write_mode = "w"
    else:
        header_text = ""
        write_mode = "a"
    save.save(data_array,"phys_quantities",header_text,write_mode)
    return