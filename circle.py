import pgzrun
import random

WIDTH = 300
HEIGHT = 300

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
x = 150

def draw():
    global r,g,b,x
    screen.draw.filled_circle((150,150),x,(r, g, b))

    for i in range(14):

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        x=x-10
        screen.draw.filled_circle((150,150),x,(r, g, b))

pgzrun.go()

