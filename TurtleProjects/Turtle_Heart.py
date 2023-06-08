import math
from turtle import *

def hearta(k):
    return 15 * math.sin(math.radians(k)) ** 3

def heartb(k):
    return 12 * math.cos(math.radians(k)) - 5 * math.cos(2 * math.radians(k)) - 2 * math.cos(3 * math.radians(k)) - math.cos(4 * math.radians(k))

speed(0)
bgcolor("black")
color("purple")

for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)

goto(0, 0)

penup()
goto(-30, -30)
pendown()
pensize(3)

def draw_n():
    left(90)
    forward(60)
    right(150)
    forward(70)
    left(150)
    forward(60)

draw_n()

done()
