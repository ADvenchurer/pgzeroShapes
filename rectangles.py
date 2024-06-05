import pgzrun
import random

WIDTH = 300
HEIGHT = 300

x=290
y=50

def draw():
    global x,y

    box = Rect((0,0),(x,y))
    box.center = 150,150

    screen.draw.rect(box,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    for i in range (10):
        x=x-10
        y=y+10
        
        box = Rect((0,0),(x,y))
        box.center = 150,150

        screen.draw.rect(box,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))





pgzrun.go()