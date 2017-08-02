"""
User interface file



"""
from pyglet.gl import *
from pyglet.text import Label
    

class PauseMenu(object):
    def __init__(self):
        self.items.append(Label("Paused"))
        self.reset()
