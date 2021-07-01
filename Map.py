from Mapa1 import maps
import math

class Map():
    def __init__(self):
        self.tile_size = 20
        self.grid = []
        self.wall_color = color(51,51,51)
        self.sand_color = [color(255,248,220), color(255,248,180), color(255,248,100)]
        self.water_color = [color(0,102,153), color(0,70,153), color(0,50,153)]
        self.atoleiro = [color(139,69,19), color(139,40,19), color(139,20,19)]
        self.wall_positions = []
        self.water_positions = []
        self.atoleiro_positions = []
        self.path_grid = []
    
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
       
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if(self.grid[i][j] == -1): self.wall_positions.append((i,j))

                if(self.grid[i][j] == 1):self.atoleiro_positions.append((i,j))
                
                if(self.grid[i][j] == 2):self.water_positions.append((i,j))
        
        self.clean_path_grid()
        
        return self.grid
    
    def clean_path_grid(self):
        self.path_grid = []
        for i in range(len(self.grid)):
            self.path_grid.append( [0] * len(self.grid[i]) )
    
    
    def get_terrain(self, position):
        x = math.floor(position.x/self.tile_size)
        y = math.floor(position.y/self.tile_size)
        return self.grid[int(x)][int(y)]
    

    def plot(self):
        # background(255)
        for i,x in enumerate(self.grid):
            for j,y in enumerate(self.grid[i]):
                position = PVector(i * self.tile_size, j * self.tile_size)
                if y == -1:
                    self.display(position, self.wall_color)
                elif y == 1:
                    self.display(position, self.atoleiro[self.path_grid[i][j]])
                elif y ==2:
                    self.display(position, self.water_color[self.path_grid[i][j]])
                else:
                    self.display(position, self.sand_color[self.path_grid[i][j]])
                
                
                    
    
    def display(self, position, fill_color):
        # Draw a triangle rotated in the direction of velocity
        fill(fill_color)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            rect(position.x, position.y, self.tile_size, self.tile_size)
