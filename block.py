import pyglet
import board #uses the board class to check collisions
"""
A Block class

"""


class Block(object):
    rotation = 0
    
    image = pyglet.image.load('assets/SquareBlock.png')

    def fall(self, speed):
        #self.y+=speed
        print("falling at speed %d" % speed)

    def rotate(self):
        print("rotating")
        self.rotation += 90

    #freezes the block at its current location
    def freeze(self):
        print("freeze the block")

    def collision_grid(self):
        #if there is a 1 at any position in the matrix
        #then check collisions for that location
        collision_grid = [[0,0,0],
                          [0,0,0],
                          [0,0,0]]
        
    def create_block():
        return self

    def isColliding(self):
        return False

    def check_defeat():
        return True

    def new_block():
        return Block()

    #def update(self, dt):
        
