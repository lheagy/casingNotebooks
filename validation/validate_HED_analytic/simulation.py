# Autogenerated at 2017-04-19T14:27:34.406221 on version 0.0.1
import casingSimulations

# Set up the simulation
sim = casingSimulations.run.SimulationFDEM(
    cp='CasingParameters.json',
    meshGenerator='MeshParameters.json',
    srcType='HorizontalElectricDipole',
    fields_filename='fields.npy'
)

# run the simulation 
fields = sim.run()