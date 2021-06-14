# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

from Food import Food

class Vehicle():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 5
        self.maxforce = 0.2

    def getPosition(self):
        return self.position
    
    def checkCollision(self, food):
        foodPosition = food.getPosition()
        foodWidth = food.r
        
        cl = foodPosition.x - foodWidth/2;  # left corner
        cr = foodPosition.x + foodWidth/2;  # right corner
        
        if (abs(cl - self.position.x) < self.r or abs(cr - self.position.x) < self.r):
            ct = foodPosition.y - foodWidth/2;  # Top corner
            cb = foodPosition.y + foodWidth/2;  # Bottom corner
    
            if (abs(ct - self.position.y) < self.r or abs(cb - self.position.y) < self.r):
                return True
        
        return False

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)    
