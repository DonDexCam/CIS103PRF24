#Donavan Bryant using turtle to create a smiley face

from turtle import*
import time
def main():
    speed(10)
    bgcolor('white')
    penup()
    goto(0,-200)
    pendown()
    pensize(5)
    pencolor('green')
    circle(200)
    penup()
    goto(-80,50)
    pendown()
    pencolor('red')
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(80,50)
    pendown()
    pencolor('blue')
    begin_fill()
    circle(30)
    end_fill
    penup()
    goto(-100,-100)
    pensize(30)
    pendown()
    forward(150)
    left(160)
    penup()
    
    goto(-140,-125)
    pensize(2)
    pendown()
    right(135)
    right(35)
    right(90)
    goto(2,-125)
    goto(1,-198)
    goto(-116,-125)
    

main()
    
