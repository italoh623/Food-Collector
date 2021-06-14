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
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    x = random(640)
    y = random(360)
    food = Food(x, y)

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    
    if (vehicle.checkCollision(food)):
        food.changePosition()
    
    food.display()
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
