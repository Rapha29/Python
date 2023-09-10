# você sabia que o python pode desenhar??? Salva o código e manda pra alguém especial!!!!!
import math
from turtle import *

def hearta(k):
    return 15*math.sin(k) **3

def heartb(k):
    return 12* math.cos(k) -5 * math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

speed(90)
bgcolor ("black")

for i in range (6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("pink")
    goto(0,0)
    
penup()
goto (-30, -30)
pendown()
color("purple")
pensize(3)

def draw_n():
    left(90)
    forward(60)
    right(150)
    forward(70)
    left(150)
    forward(60)
    
draw()
done()