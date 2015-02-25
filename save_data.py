"""
Save determined physical quantities or other data to an external file
data_array  : data to export
name        : filename
"""
## Import libraries
import re   # string editing tools
def save(data_array,name):
    write_data = str(data_array) + "\n"                                 # convert data to string
    write_data = re.sub(' +',' ',write_data)                            # remove exess spaces
    write_data = write_data.translate(None, '[]').replace(" ", "\n")    # remove brackets and add line breaks
    with open(name+".dat", "w") as file:                                # write to file
    	file.write(write_data)
    file.close()
    return