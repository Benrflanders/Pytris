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
    fall_speed = 25
    is_player_block = True
    
    
    def init(self, image, x, y, batch=None):
        super(Block, self).__init__(img, x, y, batch=batch)
        self.is_player_block = True
        fall_speed = 1
        
    def update(self, dt):
        if(self.is_player_block):
            self.x = self.x
            self.y = self.y - self.fall_speed
            rotation = self.rotation
            print("Player Block is updating")
        else:
            self.x = self.final_x
            self.y = self.final_y

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
        #use double for loops to check position array for
        #blocks touching the curr block
        return False

    def check_defeat(self):
        return False

    def new_block(self):
        self.final_x = self.x
        self.final_y = self.y
        self.is_player_block = False
        

    #def update(self, dt):
        
