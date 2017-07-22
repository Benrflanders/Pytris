"""
Tetirs inspired by the Atari Tetris game


Controlled block should fall one frae per second
Use wasd to move and rotate controlled block
when the controlled/current block touched the ground or another block:
    relese control and generate new block
    if any non controlled block touches the intersect line -> GAME OVER

"""
import pyglet
import block
from pyglet.window import key


#create board, blocks,
#board_image = 
#block_directory = " "
board = board.create_board(board_width, board_height)
block = block.create_block() #will take in a list of blocks

#Create main window
win = pyglet.window.Window(200, 600, caption='Pytris')



@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(window.,0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        print("Right arrow was pressed")
    elif symbol == key.LEFT:
        print("LEFT")
    elif symbol == key.DOWN:
        fall(2)
        print("DOWN")
    elif symbol == key.UP:
        print("UP")
    elif symbol == key.SPACE:
        print("SPACE")

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.DOWN:
        fall(1)

#Game updater
def update():
    #if player block is touching any blocks below


#Start Game

pyglet.app.run()
