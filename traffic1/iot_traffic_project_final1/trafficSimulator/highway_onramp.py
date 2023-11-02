from traffic_signal import *
from road import *
from curve import *
from simulation import *
from vehicle import *
from vehicle_generator import *
from window import *

from simulation import Simulation

# Create simulation
sim = Simulation()



# Curve resolution
n = 15

# Add multiple roads
sim.create_roads([
    ((-10, 108), (290, 108)),
    ((-10, 104), (290, 104)),

    ((290, 100), (-10, 100)),
    ((290, 96), (80, 96)),
    ((80, 96), (-10, 96)),

    #((101, 90), (80, 94)),
    #((160, 90), (100, 90)),

    #*curve_road((250, 10), (160, 90), (210, 90), resolution=n)
])

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [3, {"path": [0]}],
        [6, {"path": [1]}],
        
        [3, {"path": [3, 4]}],
        [6, {"path": [2]}],
   
        #[1, {"path": [*range(7, 7+n), 6, 5, 4]}]

    ]
})


# Start simulation
win = Window(sim)
win.offset = (-145, -95)
win.zoom = 8
win.run(steps_per_update=5)