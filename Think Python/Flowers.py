import turtle
import math

def divide(t, splits, r, a):
    angle = 0
    for i in range(splits):
         t.setheading(angle)
         petal(t, r, a)
         angle = angle + (360.0/splits)

def petal(t, r, a):
    t.right(a/2)
    t.circle(r, a)
    t.right(a)
    t.circle(-r, -a)
    home(t)
    
def home(t):
    t.pu()
    t.home()
    t.pd()
           
if __name__ == '__main__':
    bob = turtle.Turtle()
    splits = 20
    radius = 800
    angle = 15
    home(bob)
    divide(bob, splits, radius, angle)
    bob.pu()
    turtle.mainloop()