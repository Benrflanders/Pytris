import pyglet
from pyglet import sprite
from pyglet.canvas.base import Screen
from pyglet.window import Window
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
        global win_width
        global win_height
        win_width, win_height = window.get_size()

    @window.event
    def draw(self):
        global win_width
        global win_height
        width = win_width/self.rows
        height = win_height/self.cols
        pyglet.gl.glLineWidth(2)
        pyglet.gl.glPointSize(10)
        x = 0 #x start position of board
        y = 0 #y start position of board
        for i in range(self.rows):       
            for j in range(self.cols):
                pyglet.graphics.draw(4, pyglet.gl.GL_POINTS, ('v2f', [x,y,
                                                                     x,y+height,
                                                                     x+width,y+height,
                                                                     x+width,y+height]))
                x += width
            y += height
            x = xpos

test_board = Board(10,10)

@window.event
def on_draw():
    test_board.draw()

pyglet.app.run()
