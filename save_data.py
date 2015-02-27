"""
Save determined physical quantities or other data to an external file
data_array  : data to export
name        : filename
header      : optional header string (default: blank line)
write_mode  : specify write modus e.g. w = overwrite, a = append (default: a)
"""
## Import libraries
import re   # string editing tools
import six
def save(data_array,name,header="",write_mode="a"):
    if isinstance(data_array, six.string_types):
        write_data = data_array+"\n"
    else:
        write_data = "\n".join(str(x) for x in data_array)
    with open(name+".dat", write_mode) as file:                         # write to file
        file.write(header)
        file.write(write_data)
    file.close()
    return