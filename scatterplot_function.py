import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
def scat_plot(xpos,ypos,zpos):
    fig = pylab.figure()
    ax = Axes3D(fig)

    ax.scatter(xpos, ypos, ypos)
    plt.show()