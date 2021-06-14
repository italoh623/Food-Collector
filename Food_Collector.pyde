# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food

def setup():
    #Constants
    global vehicle
    global food
    global local
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    x = random(640)
    y = random(360)
    food = Food(x, y)
    local = True

def draw():
    global local
    background(255)
    mouse = PVector(mouseX, mouseY)
    
    if (vehicle.checkCollision(food)):
        food.changePosition()
        vehicle.eat()
        vehicle.food_location = PVector(-1,-1)
    

    food.display()
    vehicle.update()
    vehicle.display()
    
    if vehicle.food_location == PVector(-1,-1):
        vehicle.locate_food(food)
    
    else:
        vehicle.arrive()

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
