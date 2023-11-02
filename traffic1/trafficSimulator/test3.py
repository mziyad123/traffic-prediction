from traffic_signal import *
from road import *
from curve import *
from simulation import Simulation
from vehicle import *
from vehicle_generator import *
from window import *

# Create simulation
sim = Simulation()

sim.create_road((300, 98), (0, 98))

# Add multiple roads
#sim.generators[0].vehicle_rate=50


win = Window(sim)
win.loop()