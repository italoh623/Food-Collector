# The "Food" class

class Food():

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.r = 20
        self.f_color = color(255,0,0)

    def getPosition(self):
        return self.position
    
    # Method to update location
    def changePosition(self):
        self.position = PVector(random(640), random(360))

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
