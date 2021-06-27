# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

from Food import Food
import time

MAX_SPEED = 2
TILE_SIZE = 20

class Vehicle():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = MAX_SPEED
        self.maxforce = 0.2
        self.food_location = PVector(-1,-1)
        self.score = 0
        self.path = []
    
    def set_path(self, path):
        self.path = path

    def getPosition(self):
        return self.position
    
    def eat(self):
        self.score = self.score + 1
    
    def change_speed(self, type):
        if type == -1:
            self.velocity = PVector(-self.velocity.x, -self.velocity.y)
        elif type == 0:
            self.maxspeed = MAX_SPEED
        elif type == 1:
            self.maxspeed = MAX_SPEED * 0.5
        elif type == 2:
            self.maxspeed = MAX_SPEED * 0.3
    
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

    def locate_food(self, food):
        for y in range(0,height):
            for x in range(0,width):
                p = str(hex(get(x,y)))
                if p == 'FFFF0000':
                    self.food_location = PVector(x + food.r/2,y + food.r/2)
                    print('found food on' + str(self.food_location))
                    return
                
    
    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def arrive(self, location):
        
        target = location
        # A vector pointing from the location to the target
        desired = target - self.position
        d = desired.mag()

        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)
    
    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        # A vector pointing from the location to the target
        desired = target - self.position

        # Scale to maximum speed
        desired.setMag(self.maxspeed)

        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)
    
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
        fill(0)
        # text('Score = ' + str(self.score), 10, 10)
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
            
   
    def draw_path(self):
        """Receives path based on the grid matrix
            -> draws the path
        """
        stroke(0)
        for i in range(0,len(self.path)-1):
             p1 = self.path[i] * TILE_SIZE
             p2 = self.path[i+1] * TILE_SIZE
             line((p1[0] * TILE_SIZE) + TILE_SIZE/2, 
                  (p1[1] * TILE_SIZE) + TILE_SIZE/2, 
                  (p2[0] * TILE_SIZE) + TILE_SIZE/2, 
                  (p2[1] * TILE_SIZE) + TILE_SIZE/2)
            
            
    def drive(self):
        p = self.path.pop(0)
        # p *= TILE_SIZE
        target = PVector((p[0] * TILE_SIZE) + TILE_SIZE/2, (p[1] * TILE_SIZE) + TILE_SIZE/2)
        print(target)
        self.position = target
        
    
             
