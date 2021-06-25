# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Map import Map
from Food import Food

def setup():
    size(640, 360)
    
    #Constants
    global vehicle
    global mapa
    global food
    
    velocity = PVector(0, 0)
    vehicle = Vehicle(50, height - 50, velocity)
    x = random(640)
    y = random(360)
    food = Food(x, y)
    
    mapa = Map()
    mapa.make_grid()
    

def draw():
    mapa.plot()
    
    if (vehicle.checkCollision(food)):
        food.changePosition()
        vehicle.eat()
        vehicle.food_location = PVector(-1,-1)
        
    food.display()
    
    vehicle.update()
    vehicle.change_speed(mapa.get_terrain(vehicle.getPosition()))
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
