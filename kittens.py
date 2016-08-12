#!/usr/bin/env python

import pyglet
window = pyglet.window.Window(fullscreen=True)
#window.set_size(1920, 1080)
pyglet.resource.path = ['/']

s1 = pyglet.resource.image('kitten1.jpeg')
s2 = pyglet.resource.image('kitten2.jpeg')
s3 = pyglet.resource.image('kitten3.jpeg')
s4 = pyglet.resource.image('kitten4.jpeg')
s5 = pyglet.resource.image('kitten5.jpeg')
s6 = pyglet.resource.image('kitten6.jpeg')
s7 = pyglet.resource.image('kitten7.jpeg')

sprites = [s1, s2, s3, s4, s5, s6, s7]

anim = pyglet.image.Animation.from_image_sequence(sprites, 1, True)
sprite = pyglet.sprite.Sprite(anim)
sprite.scale = 5.5

@window.event
def on_draw():
	window.clear()
	sprite.draw()

def update(dt):
	pass

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 0.5)
	pyglet.app.run()