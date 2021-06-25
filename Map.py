from Mapa1 import maps
import math

class Map():
    def __init__(self):
        self.tile_size = 20
        self.grid = []
        self.wall_color = color(51,51,51)
        self.sand_color = color(255,248,220)
        self.water_color = color(0,102,153)
        self.atoleiro = color(139,69,19)
    
    def make_grid(self):
        # for i in range(0, width, self.tile_size):
        #     linha = []
        #     for j in range(0, height, self.tile_size):
        #         if (i == 0 or 
        #             j == 0 or
        #             i == width - self.tile_size or 
        #             j == height - self.tile_size):

        #             linha.append(-1)
                
        #         elif i == width/2 and j == height/2:
        #             linha.append(-1)
                    
        #         else:
        #             linha.append(0)
        #     self.grid.append(linha)
        
        # print(self.grid)
        index = int(random(len(maps)))
        print("Mapa", index)
        self.grid = maps[index]
        return self.grid
    
    def get_terrain(self, position):
        x = math.floor(position.x/self.tile_size)
        y = math.floor(position.y/self.tile_size)
        return self.grid[int(x)][int(y)]
    

    def plot(self):
        background(255)
        for i,x in enumerate(self.grid):
            for j,y in enumerate(self.grid[i]):
                position = PVector(i * self.tile_size, j * self.tile_size)
                if y == -1:
                    self.display(position, self.wall_color)
                elif y == 1:
                    self.display(position, self.atoleiro)
                elif y ==2:
                    self.display(position, self.water_color)
                else:
                    self.display(position, self.sand_color)
                
                
                    
    
    def display(self, position, fill_color):
        # Draw a triangle rotated in the direction of velocity
        fill(fill_color)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            rect(position.x, position.y, self.tile_size, self.tile_size)
