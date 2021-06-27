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
    global search_type
    global algoritmo
    
    search_type = "1"
    algoritmo = "Algoritmo: BFS"
    
    mapa = Map()
    mapa.make_grid()
    
    velocity = PVector(0, 0)
    vehicle = Vehicle(50, height - 50, velocity)
    
    food = Food(0, 0)
    food.changePosition(mapa)

    path = a_search.search(search_type, food, mapa, vehicle)
    vehicle.set_path(path)
    
def draw():
    mapa.plot()
    print(algoritmo)
    text(algoritmo, 30, 30)

    if (vehicle.checkCollision(food)):
        food.changePosition(mapa)
        vehicle.eat()
        vehicle.food_location = PVector(-1,-1)
        path = a_search.search(search_type, food, mapa, vehicle)
        vehicle.set_path(path)
    
    vehicle.update()
    vehicle.change_speed(mapa.get_terrain(vehicle.getPosition()))
    
    if vehicle.path:
        vehicle.draw_path()
        vehicle.drive()
    
    food.display()
    vehicle.display()
    
    time.sleep(vehicle.speed)

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
    elif key == '1':
        set_algoritmo("Algoritmo: BFS")
        print(algoritmo)
        search_type = key
        path = a_search.search(search_type, food, mapa, vehicle)
        vehicle.set_path(path)
    elif key == '2':
        set_algoritmo("Algoritmo: A*")
        print(algoritmo)
        search_type = key
        path = a_search.search(search_type, food, mapa, vehicle)
        vehicle.set_path(path)
    elif key == '3':
        set_algoritmo("Algoritmo: Uniforme")
        print(algoritmo)
        search_type = key
        path = a_search.search(search_type, food, mapa, vehicle)
        vehicle.set_path(path)
    elif key == '4':
        set_algoritmo("Algoritmo: Guloso")
        print(algoritmo)
        search_type = key
        path = a_search.search(search_type, food, mapa, vehicle)
        vehicle.set_path(path)

def set_algoritmo(new_algoritmo):
    global algoritmo 
    algoritmo = new_algoritmo
