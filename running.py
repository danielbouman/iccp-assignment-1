"""
This function returns a message to the user in the console. This message is intended to notify the user that the simulation has
started running, and is most likely still running. This function has been optimized for speed on quadcore computers.
"""
from __future__ import print_function       # make print function work in older versions of python
def message():
    print(" ")
    print("~_____________________________________________________________________________~")
    print("  ______    __   __  __    _  __    _  ___   __    _  _______                  ")
    print(" |    _ |  |  | |  ||  |  | ||  |  | ||   | |  |  | ||       |                 ")
    print(" |   | ||  |  | |  ||   |_| ||   |_| ||   | |   |_| ||    ___|                 ")
    print(" |   |_||_ |  |_|  ||       ||       ||   | |       ||   | __                  ")
    print(" |    __  ||       ||  _    ||  _    ||   | |  _    ||   ||  | __   ___   ___  ")
    print(" |   |  | ||       || | |   || | |   ||   | | | |   ||   |_| ||   | |   | |   |")
    print(" |___|  |_||_______||_|  |__||_|  |__||___| |_|  |__||_______||___| |___| |___|")
    print("*_____________________________________________________________________________*")
    print(" ")
    print(" ")
    return