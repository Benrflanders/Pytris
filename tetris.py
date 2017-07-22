"""
Tetirs inspired by the Atari Tetris game


Controlled block should fall one frae per second
Use wasd to move and rotate controlled block
when the controlled/current block touched the ground or another block:
    relese control and generate new block
    if any non controlled block touches the intersect line -> GAME OVER

"""
import tetris
##import block
##import board
##import window
##import playerInfo
from pyglet import event, app, text
from pyglet.window import Window, key
##from pyglet.app import EventLoop
win = Window(320,640,visible=False)
hello_label = text.Label('Hello, World!', font_name = 'Times New Roman',
                   font_size = 36,
                   x=win.width/2, y=win.height/2)
"""
class My    Window:
    def __init__(self, x, y, visible=True):
        global app
        app = self
    def event(self, func):
        self.what_todo = func
    def run(self):
        self.what_todo()
    def set_visible(isVisible=True):
        visible=isVisible
"""
player_score = 0
test_block = "/assets/SquareBlock.png"

running = True

event_loop = app.EventLoop()

##def draw(): ##draw each individual sprite
    

def fall():
    print("fall!")

def getNewBlock():

    block = randomBlock()
    return block

def getNextBlock(): 
    return test_block

@event_loop.event
def on_window_close(Window):
    event_loop.exit()
    return pyglet.event.EVENT_HANDLED

@event_loop.event
def on_key_press(key):
    print("on_key_press")

@Window.event
def on_draw():
    win.clear()
    label.draw()


def main():
    ##while running:
    ##    draw()
    currBlock = test_block

    @win.event
    def on_draw():
        print("drawing...")
    
    """keys = key.KeyStateHandler()
    if keys[key.SPACE]:
        print("Space bar pressed!")
    """
    win.set_visible()
    event_loop.run()



if __name__ == '__main__':
    main()


