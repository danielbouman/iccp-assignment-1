Molecular dynamics simulation of an argos gas.

This program simulates an argon gas. The user can specify the particle density and desired temperature. The program will return
the diffusion constant, specific heat, temperature, pressure, correlation length, potential-, kinetic- and total energy.

-- Initialization

The program starts by initializing the positions and momenta of all the particles. The positions are initialized by arranging all the particles in an fcc lattice in a box of size L. The momenta are initialized by generating random numbers with a Maxwell distribution. The momenta are adjusted so that the center of mass velocity is zero. All the velocities are then scaled as to satisfy the equipartition for our desired temperature. We impose periodic boundary conditions in the box, to 'enlarge' the system and to ease calculations on reflecting on the surfaces of the box.

-- Integration of the equations of motion

To simulate the motion of the particles, we use the Velocity Verlet Method. This method is used for its ease of implementation and relative accuracy. The interaction between the particles is given by a Lennard-Jones potential. For convenience we choose the parameters sigma and epsilon of the Lennard-Jones potential as our units for length and energy, respectively. The interaction between each particle pair is calculated and supplied to the Velocity Verlet algorithm to integrate the equations of motion.

-- Equilibrium

After 2500 time steps of 0.004 reduced seconds, which in total is 10 microseconds, the system can then safely be assumed to be in equilibrium. From that point on it is possible to extract physical quantities.

-- Physical quantities

We extract the kinetic energy, potential energy, total energy, diffusion constant, correlation length, pressure and specific heat from the simulation. From these quantities we calculate the mean over the equilibrium phase and it's variance to give an idea of the accuracy/fluctuations in the simulation. The diffusion constant, correlation length, pressure and specific heat merit some additional explanation for their calculation.

- Diffusion constant
The diffusion constant is defined as D = <x^2>/t in the diffusive regime. We calculate the displacement of each particle in the
