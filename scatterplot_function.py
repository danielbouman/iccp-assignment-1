## Import libraries
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
## Define scatter plot function
def scat_plot(xpos,ypos,zpos):
    fig = pylab.figure()                # Define figure
    ax = Axes3D(fig)                    # Define axis
    ## Plot
    ax.scatter(xpos, ypos, ypos)        # Plot positions
    plt.show()                          # Display plot