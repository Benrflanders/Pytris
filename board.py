import pyglet
from pyglet import sprite

class Board(sprite.Sprite):
    width = 0
    height = 10
    img = pyglet.image.load('assets/BG.png')
    
    def __init__(self, width, height, batch=None):
        super(Board, self).__init__(self.img, x, y, batch=batch)
        self.width = width
        self.height = height
        create_board(self.width, self.height)
        
    def create_board(self):
        print("creating the game board")
        return 10
    
    def update(self, dt):
        print("updating board")

    #generates the background image based on the width and height
    #of the gameboard
    def generate_bg_image():
        single_bg_tile = pyglet.image.load('assets/SquareBlock.png')
        
        return img
