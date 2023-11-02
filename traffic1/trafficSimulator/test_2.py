from traffic_signal import *
from road import *
from curve import *
from simulation import Simulation
from vehicle import *
from vehicle_generator import *
from window import *



import threading

def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")

printit()

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((0, 100), (148, 100)),
    ((148, 100), (300, 100)),
    
    ((150, 0), (150, 98)),
    ((150, 98), (150, 200)),
])

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [1, {"path": [0, 1]}],
        [1, {"path": [0, 3]}],
        [1, {"path": [2, 3]}],
        [1, {"path": [2, 3]}]
    ]
})

sim.create_signal([[0], [2]])

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)

print("end")