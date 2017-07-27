"""
Pytirs inspired by the Atari Tetris game


Controlled block should fall one frame per second
Use the left and right arrow keys to move
Rotate block with up arrow
Speed up drop with down arrow
Space to instantly place the current block
when the controlled/current block touched the ground or another
block:
    relese control and generate new block
    if any non controlled block touches the intersect line -> GAME OVER

"""
import math
import os
import random
import sys

import pyglet
import block
from pyglet.window import key
from pyglet.text import Label

#create board, blocks,
#board_image = 
#block_directory = " "
#board = board.create_board(board_width, board_height)


#Get Resources
image = pyglet.image.load('assets/SquareBlock.png')


#main window
win = pyglet.window.Window(400, 800, caption='Pytris')
start_x = win.width/2
start_y = win.height-image.height

##player_block = pyglet.sprite.Sprite(image, x=start_x, y=start_y)
curr_block = block.Block(image, x=start_x, y=start_y)
difficulty = 1


def game_over():
    game_over_text = pyglet.text("GAME OVER",
                                       font_name='Times New Roman',
                                       font_size=32,
                                       x = 20, y=20)
    set_overlay(game_over_text)


@win.event
def on_draw():
    win.clear()
    curr_block.draw()
    #image.blit(win,0)

@win.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        print("Right arrow was pressed")
    elif symbol == key.LEFT:
        print("LEFT")
    elif symbol == key.DOWN:
        print("DOWN")
    elif symbol == key.UP:
        print("UP")
        curr_block.rotate()
    elif symbol == key.SPACE:
        print("SPACE")


#Game updater
def update(dt):
    
    #if player block is touching any blocks below
        #player_block.freeze() current block, reset player block
    if curr_block.isColliding():
        curr_block.freeze()
        if curr_block.check_defeat():
            game_over()
        else:
            curr_block.new_block()
    if curr_block.y <= 0:
        #game_over()
        print("GAME OVER")
            
pyglet.clock.schedule_interval(update, 1/60)
    
#Start Game

pyglet.app.run()
