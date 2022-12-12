from turtle import*
from random import*
import turtle
import time

#screen setup
setup(800, 500)
title("Turtle Race")
bgcolor("brown")
speed(0)

#Heading
penup()
goto(-100,205)
color("black")
write("Run Turtle Run", font=("Arial", 20, "bold"))

#Dirt
goto(-350,200)
color("blue")
begin_fill()
for i in range (2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

#finish line
gap_size =20
shape("square")
penup()

#white square rows
color("white")
for i in range(10):
    goto(250, (170 -(i * gap_size*2)))
    stamp()

#white squarea rows 2
for i in range(10):
    goto(250 + gap_size, ((210- gap_size) -(i* gap_size *2)))
    stamp()
    
#Black
color("black")
for i in range(10):
    goto(250, (190-(i * gap_size*2)))
    stamp()
#Black square row 2
for i in range (10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size *2)))
    stamp()

#turtle 1- bob
bob_turtle = Turtle()
bob_turtle.color("green")
bob_turtle.shape("turtle")
bob_turtle.shapesize(2.0)
bob_turtle.penup()
bob_turtle.goto(-300, 150)
bob_turtle.pendown()

#turtle 2- Panther
panther_turtle = Turtle()
panther_turtle.color("orange")
panther_turtle.shape("turtle")
panther_turtle.shapesize(2.0)
panther_turtle.penup()
panther_turtle.goto(-300, 50)
panther_turtle.pendown()

#turtle 3- Maggi
maggi_turtle = Turtle()
maggi_turtle.color("purple")
maggi_turtle.shape("turtle")
maggi_turtle.shapesize(2.0)
maggi_turtle.penup()
maggi_turtle.goto(-300, -50)
maggi_turtle.pendown()

#turtle 4- cena
cena_turtle = Turtle()
cena_turtle.color("red")
cena_turtle.shape("turtle")
cena_turtle.shapesize(2.0)
cena_turtle.penup()
cena_turtle.goto(-300, -150)
cena_turtle.pendown()

#pause for 1sec before racing

#move the turtles
while bob_turtle.xcor()<= 230 and panther_turtle.xcor()<= 230 and maggi_turtle.xcor() <=230 and cena_turtle.xcor() <=230:
    bob_turtle.forward(randint(1, 10))
    panther_turtle.forward(randint(1, 10))
    maggi_turtle.forward(randint(1, 10))
    cena_turtle.forward(randint(1, 10))

#celebration of winner
if bob_turtle.xcor() > panther_turtle.xcor() and bob_turtle.xcor() > maggi_turtle.xcor() and bob_turtle.xcor()> cena_turtle.xcor():
    print("bob turtle wins")
    for i in range(72):
        bob_turtle.right(5)
        bob_turtle.shapesize(3.5)
        
elif panther_turtle.xcor() > bob_turtle.xcor() and panther_turtle.xcor() > maggi_turtle.xcor() and panther_turtle.xcor()> cena_turtle.xcor():
    print("Panther turtle wins")
    for i in range(72):
        panther_turtle.right(5)
        panther_turtle.shapesize(3.5)
        
elif maggi_turtle.xcor()> panther_turtle.xcor() and maggi_turtle.xcor() > bob_turtle.xcor() and maggi_turtle.xcor()> cena_turtle.xcor():
    print("maggi turtle wins")
    for i in range(72):
        maggi_turtle.right(5)
        maggi_turtle.shapesize(3.5)
    
else:
    print("Cena turtle wins!")
    for i in range(72):
        cena_turtle.right(5)
        cena_turtle.shapesize(3.5)

