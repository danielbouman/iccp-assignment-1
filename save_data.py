"""
Save determined physical quantities or other data to an external file
data_array  : data to export
name        : filename
header      : optional header string (default: blank line)
write_mode  : specify write modus e.g. w = overwrite, a = append (default: a)
"""
## Import libraries
import re   # string editing tools
def save(data_array,name,header="",write_mode="a"):
    write_data = str(data_array) + "\n"                                 # convert data to string
    write_data = re.sub(' +',' ',write_data)                            # remove exess spaces
    write_data = write_data.translate(None, '[]').replace(" ", "\n")    # remove brackets and add line breaks
    with open(name+".dat", write_mode) as file:                         # write to file
        if write_mode == "w":
            file.write(header)
    	file.write(write_data)
    file.close()
    return