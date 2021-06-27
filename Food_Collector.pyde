# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Map import Map
from Food import Food
import a_search
import time

def setup():
    size(640, 360)
    
    global mapa
    global vehicle
    global food
    global path
    
    velocity = PVector(0, 0)
    vehicle = Vehicle(40, height - 40, velocity)
    x = random(640)
    y = random(360)
    food = Food(x, y)
    
    mapa = Map()
    mapa.make_grid()
    
    velocity = PVector(0, 0)
    vehicle = Vehicle(50, height - 50, velocity)
    
    food = Food(0, 0)
    food.changePosition(mapa)

    path = a_search.a_search(food, mapa, vehicle)
    
def draw():
    mapa.plot()

    if (vehicle.checkCollision(food)):
        food.changePosition(mapa)
        vehicle.eat()
        vehicle.food_location = PVector(-1,-1)
    
    vehicle.update()
    vehicle.change_speed(mapa.get_terrain(vehicle.getPosition()))
    
    food.display()
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
    elif key == 'p':
        vehicle.walk_path([PVector(2,16), PVector(3,16), PVector(4,16), PVector(5,16), PVector(6,16), PVector(7,16), PVector(8,16), PVector(9,16)])
