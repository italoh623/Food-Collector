# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Map import Map

def setup():
    size(640, 360)
    
    #Constants
    global vehicle
    global mapa
    
    velocity = PVector(1, 0)
    vehicle = Vehicle(50, height - 50, velocity)
    x = random(640)
    y = random(360)
    mapa = Map()
    mapa.make_grid()
    

def draw():
    mapa.plot()
    vehicle.update()
    vehicle.display()


def keyTyped():
    print(key)
    if key == 'a':
        vehicle.applyForce(PVector(-0.1,0.0))
    elif key == 'd':
        vehicle.applyForce(PVector(0.1,0.0))
    elif key == 'w':
        vehicle.applyForce(PVector(0.0,-0.1))
    elif key == 's':
        vehicle.applyForce(PVector(0.0,0.1))
