import pyglet
from pyglet.window import key


window = pyglet.window.Window()
#image = pyglet.resource.image('assets/SquareBlock.png')
image = pyglet.image.load('assets/SquareBlock.png')

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

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




pyglet.app.run()
