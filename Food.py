# The "Food" class
import math

class Food():

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.r = 20
        self.f_color = color(255,0,0)

    def getPosition(self):
        return self.position
    
    # Method to update location
    def changePosition(self, mapa):
        PositionX = random(width)
        PositionY = random(height)
        
        x = int(math.floor(PositionX / mapa.tile_size))
        y = int(math.floor(PositionY / mapa.tile_size))
        
        while mapa.grid[x][y] != 0:
            PositionX = random(width)
            PositionY = random(height)
            
            x = int(math.floor(PositionX / mapa.tile_size))
            y = int(math.floor(PositionY / mapa.tile_size))
        
        self.position = PVector(x * mapa.tile_size, y * mapa.tile_size)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        fill(self.f_color)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rect(0, 0, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)
