# Autogenerated at 2017-04-28T16:10:05.219470 on version 0.0.1
import casingSimulations
import numpy as np

# Set up the simulation
sim = casingSimulations.run.SimulationTDEM(
    cp='CasingParameters.json',
    meshGenerator='MeshParameters.json',
    src='Source.json',
    fields_filename='fields.npy'
)

# run the simulation 
fields = sim.run()

# Set up a 2D simulation for the same source location
mesh2D = sim.meshGenerator.copy()
mesh2D.hy = np.r_[2*np.pi]
src2D = getattr(casingSimulations.sources, sim.src.__class__.__name__)(
    cp=sim.cp,
    meshGenerator=mesh2D,
)
sim2D = casingSimulations.run.SimulationTDEM(
    cp=sim.cp,
    meshGenerator=mesh2D,
    src=src2D,
    fields_filename='fields2D.npy',
    filename='simulation2D.json'
)

# run the 2D simulation 
fields2D = sim2D.run()

# Set up DC survey for the same source location
csz = sim.meshGenerator.csz
# make sure it is in the cell
src_a = sim.src.src_a_closest - np.r_[0., 0., csz/2.]
src_b = sim.src.src_b_closest - np.r_[0., 0., csz/2.]

simDC = casingSimulations.run.SimulationDC(
    filename='simulationDC.py',
    cp=sim.cp,
    meshGenerator=sim.meshGenerator,
    src_a=src_a,
    src_b=src_b
)
# run the DC simulation 
fieldsDC = simDC.run()
