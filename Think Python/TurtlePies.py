import turtle

sides = 7
radius = 100
angle = 360.0/sides
temp = 270
bob = turtle.Turtle()
bob.circle(radius, 360, sides)
bob.setheading(90)
bob.pu()
bob.forward(radius)
bob.pd()
for i in range(sides):
    bob.setheading(temp)
    bob.forward(radius)
    bob.backward(radius)
    temp = temp + angle
turtle.mainloop()