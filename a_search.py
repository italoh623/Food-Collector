# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

# some of these types are deprecated: https://www.python.org/dev/peps/pep-0585/

import time

class Graph():
    def neighbors(self, id ): pass

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id ):
        return self.edges[id]

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['C'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': [],
}

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return not self.elements
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()
    

class Stack:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return not self.elements
    
    def push(self, x):
        self.elements.append(x)
    
    def pop(self):
        return self.elements.pop()

# utility functions for dealing with square grids
def from_id_width(id, width):
    return (id % width, id // width)

def draw_tile(graph, id, style):
    r = " . "
    if 'number' in style and id in style['number']: r = " %-2d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = " > "
        if x2 == x1 - 1: r = " < "
        if y2 == y1 + 1: r = " v "
        if y2 == y1 - 1: r = " ^ "
    if 'path' in style and id in style['path']:   r = " @ "
    if 'start' in style and id == style['start']: r = " A "
    if 'goal' in style and id == style['goal']:   r = " Z "
    if id in graph.walls: r = "###"
    return r

def draw_grid(graph, **style):
    
    print("___" * graph.width)
    for y in range(graph.height):
        stri = ""
        for x in range(graph.width):
            stri = stri + draw_tile(graph, (x, y), style)
            #print("%s" % draw_tile(graph, (x, y), style), end="")
        print(stri)
    print("~~~" * graph.width)

# data from main article
DIAGRAM1_WALLS = [from_id_width(id, width=30) for id in [21,22,51,52,81,82,93,94,111,112,123,124,133,134,141,142,153,154,163,164,171,172,173,174,175,183,184,193,194,201,202,203,204,205,213,214,223,224,243,244,253,254,273,274,283,284,303,304,313,314,333,334,343,344,373,374,403,404,433,434]]

GridLocation = []

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results

class WeightedGraph(Graph):
    def cost(self, from_id , to_id ): pass

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results
        
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

diagram4 = GridWithWeights(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
diagram4.weights.update({loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2)]})
diagram4.weights.update({loc: 10 for loc in [(1, 4), (1, 5), (2, 1), (2, 2)]})


import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return not self.elements
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def dijkstra_search(graph, start , goal, mapa):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current  = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            mapa.path_grid[next[0]][next[1]] = 1
            mapa.path_grid[current[0]][current[1]] = 2
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

# thanks to @m1sp <Jaiden Mispy> for this simpler version of
# reconstruct_path that doesn't have duplicate entries

def reconstruct_path(came_from, start , goal ):
    current  = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start , goal, mapa):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current  = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            mapa.path_grid[next[0]][next[1]] = 1
            mapa.path_grid[current[0]][current[1]] = 2
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def depth_first_search(graph, start , goal, mapa):
    frontier = Stack()
    frontier.push(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current  = frontier.pop()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            mapa.path_grid[next[0]][next[1]] = 1
            mapa.path_grid[current[0]][current[1]] = 2
            if next not in came_from:
                frontier.push(next)
                came_from[next] = current
        
    return came_from

def breadth_first_search(graph, start , goal, mapa):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current  = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            mapa.path_grid[next[0]][next[1]] = 1
            mapa.path_grid[current[0]][current[1]] = 2
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from

class SquareGridNeighborOrder(SquareGrid):
    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x + dx, y + dy) for (dx, dy) in self.NEIGHBOR_ORDER]
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return list(results)

def test_with_custom_order(neighbor_order):
    if neighbor_order:
        g = SquareGridNeighborOrder(30, 15)
        g.NEIGHBOR_ORDER = neighbor_order
    else:
        g = SquareGrid(30, 15)
    g.walls = DIAGRAM1_WALLS
    start, goal = (8, 7), (27, 2)
    came_from = breadth_first_search(g, start, goal)
    draw_grid(g, path=reconstruct_path(came_from, start=start, goal=goal),
              point_to=came_from, start=start, goal=goal)

class GridWithAdjustedWeights(GridWithWeights):
    def cost(self, from_node, to_node):
        prev_cost = super().cost(from_node, to_node)
        nudge = 0
        (x1, y1) = from_node
        (x2, y2) = to_node
        if (x1 + y1) % 2 == 0 and x2 != x1: nudge = 1
        if (x1 + y1) % 2 == 1 and y2 != y1: nudge = 1
        return prev_cost + 0.001 * nudge

def a_search(food, mapa, vehicle): 
    a_food = food.position/mapa.tile_size
    a_vehicle = vehicle.position/mapa.tile_size

    start, goal = (floor(a_vehicle[0]), floor(a_vehicle[1])), (a_food[0], a_food[1])
    
    mapa_a = GridWithWeights(len(mapa.grid), len(mapa.grid[0]))
    mapa_a.walls = mapa.wall_positions
    mapa_a.weights.update({loc: 5 for loc in mapa.atoleiro_positions})
    mapa_a.weights.update({loc: 10 for loc in mapa.water_positions})
    
    came_from, cost_so_far = a_star_search(mapa_a, start, goal, mapa)
    
    #draw_grid(mapa_a, point_to=came_from, start=start, goal=goal)
    draw_grid(mapa_a, path=reconstruct_path(came_from, start=start, goal=goal))
    #draw_grid(mapa_a, number=cost_so_far, start=start, goal=goal) 
    return reconstruct_path(came_from, start=start, goal=goal)

def bfs_search(food, mapa, vehicle): 
    a_food = food.position/mapa.tile_size
    a_vehicle = vehicle.position/mapa.tile_size

    start, goal = (floor(a_vehicle[0]), floor(a_vehicle[1])), (a_food[0], a_food[1])
    
    mapa_a = GridWithWeights(len(mapa.grid), len(mapa.grid[0]))
    mapa_a.walls = mapa.wall_positions
    
    parents = breadth_first_search(mapa_a, start, goal, mapa)
    #draw_grid(mapa_a, point_to=parents, start=start, goal=goal)
    #draw_grid(mapa_a, path=reconstruct_path(parents, start=start, goal=goal))
    return reconstruct_path(parents, start=start, goal=goal)

def dfs_search(food, mapa, vehicle): 
    a_food = food.position/mapa.tile_size
    a_vehicle = vehicle.position/mapa.tile_size

    start, goal = (floor(a_vehicle[0]), floor(a_vehicle[1])), (a_food[0], a_food[1])
    
    mapa_a = GridWithWeights(len(mapa.grid), len(mapa.grid[0]))
    mapa_a.walls = mapa.wall_positions
    
    parents = depth_first_search(mapa_a, start, goal, mapa)
    #draw_grid(mapa_a, point_to=parents, start=start, goal=goal)
    draw_grid(mapa_a, path=reconstruct_path(parents, start=start, goal=goal))
    return reconstruct_path(parents, start=start, goal=goal)

def dijkstra(food, mapa, vehicle): 
    a_food = food.position/mapa.tile_size
    a_vehicle = vehicle.position/mapa.tile_size

    start, goal = (floor(a_vehicle[0]), floor(a_vehicle[1])), (a_food[0], a_food[1])
    
    mapa_a = GridWithWeights(len(mapa.grid), len(mapa.grid[0]))
    mapa_a.walls = mapa.wall_positions
    mapa_a.weights.update({loc: 5 for loc in mapa.atoleiro_positions})
    mapa_a.weights.update({loc: 10 for loc in mapa.water_positions})

    came_from, cost_so_far = dijkstra_search(mapa_a, start, goal, mapa)
    #draw_grid(mapa_a, point_to=came_from, start=start, goal=goal)
    #draw_grid(mapa_a, path=reconstruct_path(came_from, start=start, goal=goal))
    #draw_grid(mapa_a, number=cost_so_far, start=start, goal=goal)
    return reconstruct_path(came_from, start=start, goal=goal)    

def search(type, food, mapa, vehicle):
    if type == "1":
        return bfs_search(food, mapa, vehicle)
    elif type == "2":
        return a_search(food, mapa, vehicle)
    elif type == "3":
        return dijkstra(food, mapa, vehicle)
    elif type == "4":
        return heuristc_search(food, mapa, vehicle)
    elif type == "5":
        return dfs_search(food, mapa, vehicle)

def heuristc_algorithm(graph, start , goal, mapa):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
    
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                mapa.path_grid[next[0]][next[1]] = 1
                mapa.path_grid[current[0]][current[1]] = 2
                priority = heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from
                
def heuristc_search(food, mapa, vehicle): 
    a_food = food.position/mapa.tile_size
    a_vehicle = vehicle.position/mapa.tile_size

    start, goal = (floor(a_vehicle[0]), floor(a_vehicle[1])), (a_food[0], a_food[1])
    
    mapa_a = GridWithWeights(len(mapa.grid), len(mapa.grid[0]))
    mapa_a.walls = mapa.wall_positions
    mapa_a.weights.update({loc: 5 for loc in mapa.atoleiro_positions})
    mapa_a.weights.update({loc: 10 for loc in mapa.water_positions})

    came_from =  heuristc_algorithm(mapa_a, start, goal, mapa)
    draw_grid(mapa_a, point_to=came_from, start=start, goal=goal)
    draw_grid(mapa_a, path=reconstruct_path(came_from, start=start, goal=goal))
    #draw_grid(mapa_a, number=cost_so_far, start=start, goal=goal)
    return reconstruct_path(came_from, start=start, goal=goal)    
