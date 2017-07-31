import pyglet
import board #uses the board class to check collisions
from pyglet import sprite


"""
A Block class, an extension of a sprite

"""



class Block(sprite.Sprite):
    dx = 0
    dy = 0
    rotation = 0
    fall_speed = 1

    
    def init(self, image, x, y, batch=None):
        super(Block, self).__init__(img, x, y, batch=batch)

    def update(self, dt):
        x = self.x + fall_speed
        y = self.y
        rotation = self.rotation

    def rotate(self):
        print("rotating")
        self.rotation += 90

    #freezes the block at its current location
    def freeze(self):
        print("freeze the block")


    def create_block():
        return self

    def isColliding(self):
        return False

    def check_defeat():
        #if block is stopped: board.checkGameOver(self)
        return True

    def new_block():
        return Block()

    #def update(self, dt):


    
