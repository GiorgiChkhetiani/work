from turtle import *

#we want to point house
#step 1: draw a square 

width (7)
color ("orange")

forward(200)
left (90) 

forward (200)
left(90)

forward(200)
left(90)
 
forward (200)
left(90)


forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()

goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(30,30)
pendown()
color("orange")
begin_fill()
right(150) 
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)

penup()
goto(150,30)
pendown()
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
end_fill()

penup()
goto(30,110)
pendown()
color("orange")
begin_fill()
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
end_fill()

penup()
goto(150,110)
pendown()
color('orange')
begin_fill()
right(90)
forward(40)
right(90)
forward(20)
right(90)

forward(40)
right(90)
forward(20)
end_fill()


exitonclick()




