import pyglet
import random

win=pyglet.window.Window(width=500, height=500, caption="Dragon Game")
dragon=pyglet.image.load("dragon.png")

dragon.anchor_x=dragon.width/2
dragon.anchor_y=dragon.height/2

dragon_x = random.randint(0, win.width-dragon.width)
dragon_y = random.randint(0, win.height-dragon.height)

@win.event
def on_mouse_press(x, y, button, modifier):

    mouse_x_in_image_area= x>=(dragon_x - dragon.width/2) and x<=(dragon_x + dragon.width/2)
    mouse_y_in_image_area= y>=(dragon_y - dragon.height/2) and y<=(dragon_y + dragon.height/2)

    if button == pyglet.window.mouse.LEFT and mouse_x_in_image_area and mouse_y_in_image_area:

	print"dragon jeet gya"
    else:
	print "aap jeet gye"

@win.event
def on_draw():
    dragon.blit(dragon_x, dragon_y)

pyglet.app.run()
