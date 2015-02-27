Molecular dynamics simulation of an argon gas.

-- Execution
To run, compile main.py. Tested with python versions 2.7.6 and 3.4. 

-- User input and output
This program simulates an argon gas. The user can specify the particle density and desired temperature. The program will return the diffusion constant, specific heat, temperature, pressure, correlation length, potential-, kinetic- and total energy as a function of timesteps, in corresponding .dat files. The average and variance values of temperature, pressure, potential energy, specif heat, total energy and diffusion constant are saved to phys_quantities.dat.

-- Important notes for the user
Equilibrium of the system is achieved around 2500 time steps. Therefore only for times larger than 2500, will phy_quantities.dat be generated. For reliable quantities, a minimum of 5000 time steps is recommended.

-- General outline of the program -- 

-- Initialization
The program starts by initializing the positions and momenta of all the particles. The positions are initialized by arranging all the particles in an fcc lattice in a box of size L. The momenta are initialized by generating random numbers with a Maxwell distribution. The momenta are adjusted so that the center of mass velocity is zero. All the velocities are then scaled as to satisfy the equipartition for our desired temperature. We impose periodic boundary conditions in the box, to 'enlarge' the system and to ease calculations on reflecting on the surfaces of the box.

-- Integration of the equations of motion
To simulate the motion of the particles, we use the Velocity Verlet Method. This method is used for its ease of implementation and relative accuracy. The interaction between the particles is given by a Lennard-Jones potential. For convenience we choose the parameters sigma and epsilon of the Lennard-Jones potential as our units for length and energy, respectively. The interaction between each particle pair is calculated and supplied to the Velocity Verlet algorithm to integrate the equations of motion.

-- Equilibrium
After 2500 time steps of 0.004 reduced seconds, which in total is 10 microseconds, the system can then safely be assumed to be in equilibrium. From that point on it is possible to extract physical quantities.

-- Physical quantities
We extract the kinetic energy, potential energy, total energy, diffusion constant, correlation length, pressure and specific heat from the simulation. From these quantities we calculate the mean over the equilibrium phase and it's variance to give an idea of the accuracy/fluctuations in the simulation. The diffusion constant, correlation length, pressure and specific heat merit some additional explanation for their calculation.

- Diffusion constant
The diffusion constant D is defined as <x^2> = Dt in the diffusive regime. We calculate the displacement of each particle in the x,y,z direction, taking into account periodic boundary conditions. Dividing the displacement by the time step allows us to find the instanteneous diffusion constant

- Correlation length
At the beginning of the simulation, an array is initialized with linear spacing from 0 to (sqrt(3)/2)*L (the maximum distance allowed before periodic boundary conditions kick in) with 1000 elements. During each time step, an array is created with all the absolute distances in it. A histogram is created by splitting the second list into the 'bins' of the first list. This histogram is saved every timestep. After the end of the simulation, we can calculate the average amount of particles over the time per bin. Using the formula given, this allows us to find the correlation length.

- Pressure
The pressure is calculated by a virial expansion. The total virial is calculated every time step. An additional correction is used when a cutoff is implemented

- Specific heat
The specific heat is calculated every time step by a formula derived by Lebowitz et al (Ensemble Dependence of Fluctuations with Application to Machine Computation)








