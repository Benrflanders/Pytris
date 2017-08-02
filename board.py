import pyglet
from pyglet import sprite
from pyglet.gl import *

window = pyglet.window.Window() #window for testing block class



'''
'   board draws the background grid and checks for collisions between blocks
'   and the game over line
'''
class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        #self.create_board(0,0, 4, 4)

    @window.event
    def draw(self, xpos, ypos, width, height):
        pyglet.gl.glLineWidth(5)
        x = xpos
        y = ypos
        for i in range(self.rows):
                        
            for j in range(self.cols):
                pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [x,y,
                                                                     x,-y,
                                                                     -x,-y,
                                                                     -x,y]))
                x -= width
            y -= height 

    #a single grid square, used for generating the background grid
    def create_grid_square(width, height, xpos, ypos):
        verts = [] #list of vertecies for the individual grid square
        self.xpos = xpos
        self.ypos = ypos
        self.angle = 0
        self.size = 1
        x = width/2.0
        y = height/2.0
        verts += [(x,y),(x,-y),(-x,-y),(-x,y)]
            
    def draw_old(self, width, height, x, y):
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        square = pyglet.graphics.vertex_list(4,('v2f', verts)) 
        

test_board = Board(10,10)

@window.event
def on_draw():
    test_board.draw(0,0, 10, 10)

pyglet.app.run()
