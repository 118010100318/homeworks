from turtle import *
from math import *
#绘制方框
setup(600,400,200,200)
begin_fill()
fillcolor("red")
penup()
goto(-300,200)
pendown()
for i in range(2):
    fd(600)
    right(90)
    fd(400)
    right(90)
end_fill()
#绘制最大的星
seth(0)
penup()
goto(-200,160)
pendown()
begin_fill()
fillcolor("yellow")
for i in range(5):
    right(72)
    fd(40/sin(radians(72)))
    left(72)
    fd(40/sin(radians(72)))
    right(72)
end_fill()
#绘制从上到下的第一个星
seth(0)
penup()
goto(-100,160)
left(degrees(atan(3/5))+180)
fd(20)
left(180)
begin_fill()
fillcolor("yellow")
pendown()
for i in range(5):
    right(18)
    fd(40/3*sin(radians(72)))
    right(72)
    fd(40/3*sin(radians(72)))
    left(162)
end_fill()
#绘制从上到下的第二个星
seth(0)
penup()
goto(-60,120)
left(degrees(atan(1/7))+180)
fd(20)
left(180)
begin_fill()
fillcolor("yellow")
pendown()
for i in range(5):
    right(18)
    fd(40/3*sin(radians(72)))
    right(72)
    fd(40/3*sin(radians(72)))
    left(162)
end_fill()
#绘制从上到下的第三个星
seth(0)
penup()
goto(-60,60)
right(degrees(atan(2/7))+180)
fd(20)
left(180)
begin_fill()
fillcolor("yellow")
pendown()
for i in range(5):
    right(18)
    fd(40/3*sin(radians(72)))
    right(72)
    fd(40/3*sin(radians(72)))
    left(162)
end_fill()
#绘制从上到下的第四个星
seth(0)
penup()
goto(-100,20)
right(degrees(atan(4/5))+180)
fd(20)
left(180)
begin_fill()
fillcolor("yellow")
pendown()
for i in range(5):
    right(18)
    fd(40/3*sin(radians(72)))
    right(72)
    fd(40/3*sin(radians(72)))
    left(162)
end_fill()
penup()
goto(300,200)
