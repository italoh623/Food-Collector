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

quantidade = 0

def setup():
    size(640, 360)
    global mapa
    global vehicle
    global food
    global path
    global search_type
    global algoritmo
    global contexto
    global sett
    global valor
    global conjunto
    global liga
    liga = 0
    contexto = []
    conjunto = []
    sett = 0
    valor = 0
    
    search_type = "1"
    algoritmo = "Algoritmo: BFS"
    mapa = Map()
    mapa.make_grid()
    
    velocity = PVector(0, 0)
    vehicle = Vehicle(50, height - 50, velocity)
    
    food = Food(0, 0)
    food.changePosition(mapa)

    print(algoritmo)
    #path = a_search.search(search_type, food, mapa, vehicle, conjunto, contexto, 0)
    #vehicle.set_path(path)
    
def draw():
    global sett
    global vetorzinho
    global conjunto
    global contexto
    global valor
    global camefrom
    global liga
    mapa.plot()
    #print(algoritmo)
    text(algoritmo, 30, 30)
    #if()
    retorno,camefrom,valor = a_search.search(search_type, food, mapa, vehicle, conjunto, contexto, sett, liga)
    sett = 1
    contexto = retorno
    if(valor == 1):
        caminho = camefrom
        liga = 1
    
    fill(230, 124, 24, 80);
    for j in conjunto : #printar os tiles até aquele momento
        rect(j[0]*20, j[1]*20, 20, 20)
        
    if(valor == 1):
        a_food = food.position/20
        a_vehicle = vehicle.position/20
            
        start, goal = (floor(a_vehicle[0]), floor(a_vehicle[1])), (a_food[0], a_food[1])
        path = a_search.reconstruct_path(caminho, start, goal)
        vehicle.set_path(path)
        #time.sleep(vehicle.speed)
    
    
    if (vehicle.checkCollision(food)):
        print(algoritmo)
        food.changePosition(mapa)
        vehicle.eat()
        vehicle.food_location = PVector(-1,-1)
        conjunto = []
        contexto = []
        sett = 0
        liga = 0
        global quantidade
        quantidade = quantidade + 1
        vetorzinho = []
        valor = 0
    
    vehicle.update()
    vehicle.change_speed(mapa.get_terrain(vehicle.getPosition()))
    
    if vehicle.path:
        vehicle.draw_path()
        vehicle.drive()
    
    food.display()
    vehicle.display()
    
    fill(255, 255, 255)
    noStroke()
    strokeWeight(1)
    with pushMatrix():
        translate(400, 15)
        string = str(quantidade) + " Comida(s) foram coletadas"
        text(string, 0,0)
    if(liga == 0):
        time.sleep(vehicle.speed/10)
    elif(liga == 1):
        #print('aaaaaaa')
        time.sleep(vehicle.speed)

def keyTyped():
    global mapa
    global vehicle
    global food
    global path
    global search_type
    global algoritmo
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
        limpavalores()
    elif key == '2':
        #limpavalores()
        set_algoritmo("Algoritmo: A*")
        print(algoritmo)
        search_type = key
        #retorno,camefrom,valor = a_search.search(search_type, food, mapa, vehicle, conjunto, contexto, sett, liga)
        limpavalores()
    elif key == '3':
        set_algoritmo("Algoritmo: Uniforme")
        print(algoritmo)
        search_type = key
        limpavalores()
    elif key == '4':
        set_algoritmo("Algoritmo: Guloso")
        print(algoritmo)
        search_type = key
        limpavalores()
    elif key == '5':
        set_algoritmo("Algoritmo: DFS")
        print(algoritmo)
        search_type = key
        limpavalores()
    elif key == 'c':
        food.changePosition(mapa)
        #vehicle.eat()
        vehicle.food_location = PVector(-1,-1)
        limpavalores()
        #path = a_search.search(search_type, food, mapa, vehicle)
        #vehicle.set_path(path)
        
    elif key == 'r':
        mapa = Map()
        mapa.make_grid()
        
        #search_type = "1"
        set_algoritmo(algoritmo)
        
        food.changePosition(mapa)

        limpavalores()

def set_algoritmo(new_algoritmo):
    global algoritmo 
    algoritmo = new_algoritmo
    
def limpavalores():
    global sett
    global conjunto
    global contexto
    global valor
    global camefrom
    global liga
    conjunto = []
    contexto = []
    sett = 0
    liga = 0
    valor = 0
    sett = 0
