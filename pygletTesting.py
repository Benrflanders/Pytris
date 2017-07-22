import pyglet

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
    image.blit(0,0)

pyglet.app.run()
