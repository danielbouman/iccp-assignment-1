## Import libraries
import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold='nan')
import datetime
## Import functions
from initpos_function import initpos
from initvelocity import initvelocity
from velocity_verlet import velocity_verlet
from normalize_momentum import normalize_momentum
from store_quantities import store_quantities
## Assign variables
L = 20                      # Box length
M = 1                       # Unit cells per dimension
N = 4*np.power(M,3)         # Number of particles, 4 per unit cell
h = 0.01 					# Timestep
T = 200                     # Temperature
m = 1                       # Particle mass


display_data = raw_input('Write to file (w) or plot (p):') or 'w'
time_dur = raw_input('Timesteps:') or 5000         # In units of timesteps
time_dur = int(time_dur)

time_step = np.zeros((time_dur),dtype=float)
vel_time = np.zeros((time_dur),dtype=float)
pos_time = np.zeros((time_dur),dtype=float)
time = np.zeros((time_dur),dtype=float)
kin_energy = np.zeros((time_dur),dtype=float)
total_velocity = np.zeros((time_dur),dtype=float)
pot_energy = np.zeros((time_dur),dtype=float)
total_energy = np.zeros((time_dur),dtype=float)


## Init particle positions
pos = initpos( L,N,M )

## Init velocity
velocity = initvelocity( N, T ,m )

## Init acceleration
a_0 = np.zeros((N,3),dtype=float) #Initialize acceleration array

## Write timestamp to output file
current_time = datetime.datetime.now()
with open("pot_energy.dat", "w") as fh:
    fh.write("\n# "+current_time.strftime('%Y/%m/%d %H:%M:%S')+":\n\n")
fh.close()
with open("kin_energy.dat", "w") as fh:
    fh.write("\n# "+current_time.strftime('%Y/%m/%d %H:%M:%S')+":\n\n")
fh.close()
with open("total_energy.dat", "w") as fh:
    fh.write("\n# "+current_time.strftime('%Y/%m/%d %H:%M:%S')+":\n\n")
fh.close()

## Plotting
# fig = plt.figure()  # Define figure
    
## Time evolution
for t in xrange(0, time_dur):
    pos,velocity,a_0,potential = velocity_verlet( N, h, pos, velocity, a_0, L )
    time_step[t] = t*h
    pot_energy[t] = sum(potential)
    print velocity
    kin_energy[t] = sum(sum(0.5*(np.power(velocity,2))))
    print kin_energy[t]
    total_energy[t] = np.add(kin_energy[t],pot_energy[t])
    if np.mod(t,200) == 0:
    	velocity = normalize_momentum(N, velocity,T)
    #total_energy[t] = np.add(kin_energy,pot_energy)
    ## Dynamic plotting
    # time[t] = t 
    # pos_time[t] = pos[0,1]
    # plt.xlim([0,L])
    # plt.ylim([0,L])
    # plt.show()
    # ax = Axes3D(fig)                            # Define axis
    # ax.scatter(pos[:,0], pos[:,1], pos[:,2])    # Plot positions#
    ## Print
    # print velocity[0,0]
    # print kin_energy[t]
    # print pos[1,2]
    ## Write to output file
    # out_vel = str(pot_energy[1,2]) + "\n"
    # with open("output.dat", "a") as fh:
    #     fh.write(out_vel)
	if display_data == 'w':
		out_energ = str(total_energy[t]) + "\n"
		out_energ = out_energ.translate(None, '[]').replace(" ", "")
		with open("total_energy.dat", "a") as f_energ:
			f_energ.write(out_energ)
		f_energ.close()
		out_kin = str(kin_energy[t]) + "\n"
		out_kin = out_kin.translate(None, '[]').replace(" ", "")
		with open("kin_energy.dat", "a") as f_kin:
			f_kin.write(out_kin)
		f_kin.close()
		out_pot = str(pot_energy[t]) + "\n"
		out_pot = out_pot.translate(None, '[]').replace(" ", "")
		with open("pot_energy.dat", "a") as f_pot:
			f_pot.write(out_pot)
		f_pot.close() # Close output file
		
if display_data == 'p':
	plt.plot(time_step,pot_energy, 'r')
	plt.show()
	plt.plot(time_step,kin_energy, 'b')
	plt.show()
	plt.plot(time_step,total_energy, 'g')
	plt.show()
