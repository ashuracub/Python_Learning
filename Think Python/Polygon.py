from __future__ import print_function, division

import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(  t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle)/360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    arc(t, r, 360)

if __name__ == '__main__':
    bob = turtle.Turtle()
    circle(bob, 150)
    turtle.mainloop()