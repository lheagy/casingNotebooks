import casingSimulations

# Set up the simulations

# Cylindrically symmetric
sim2D = casingSimulations.run.SimulationFDEM(
    cp='CasingParameters.json',
    meshGenerator='mesh2D.json',
    srcType='DownHoleCasingSrc',
    fields_filename='fields2D.npy',
    simulation_filename='sim2D.json',
    num_threads=12
)

# 3D Cyl Simulation
sim3D = casingSimulations.run.SimulationFDEM(
    cp='CasingParameters.json',
    meshGenerator='mesh3D.json',
    srcType='DownHoleCasingSrc',
    fields_filename='fields3D.npy',
    simulation_filename='sim3D.json',
    num_threads=12
)

# run the simulations
fields2D = sim2D.run()
fields3D = sim3D.run()
