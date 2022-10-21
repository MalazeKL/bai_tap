import turtle

t=turtle.Pen()
turtle.bgcolor("cyan")
t.pensize(3)

t.penup()
t.goto(-200,-100)
t.pendown()
# mặt trước căn nhà
t.fillcolor("blue")
t.begin_fill()
for i in range(0,2):
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(130)
t.end_fill()
# mặt phải căn nhà
t.fillcolor("yellow")
t.begin_fill()
for i in range(0,2):
    if i == 0:
        t.lt(40)
    else:
        t.lt(130)
    t.fd(90)
    t.lt(50)
    t.fd(150)
t.end_fill()
t.rt(90)
t.fd(50)
#cửa nhà
t.fillcolor("aqua")
t.begin_fill()
for i in range(0,2):
    if i == 0:
        t.rt(90)
    else:
        t.lt(90)
    t.fd(90)
    t.lt(90)
    t.fd(40)
t.end_fill()
t.fd(50)
#cửa sổ
t.penup()
t.goto(-160, 30)
t.pendown()
t.fillcolor("red")
t.begin_fill()
for i in range(0,2):
    if i == 0:
        t.rt(90)
    else:
        t.rt(130)
    t.fd(45)
    t.rt(50)
    t.fd(27)
t.end_fill()
#mái
t.lt(50)
t.penup()
t.goto(-200,50)
t.pendown()
#phần mái trái
t.fillcolor("hot pink")
t.begin_fill()
t.lt(45)
t.fd(90)
t.backward(90)
t.lt(45)
t.fd(130)
t.rt(135)
t.fd(90)
t.end_fill()
#phần mái phải
t.fillcolor("orange")
t.begin_fill()
t.fd(90)
t.rt(89)
t.fd(100)
t.right(96)
t.fd(90)
t.rt(85)
t.fd(92)
t.end_fill()
t.rt(135)
#lá cây
y = 100
for i in range(0,3):
    t.penup()
    t.goto(100,y)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.lt(140)
    t.backward(50)
    t.lt(40)
    t.fd(80)
    t.rt(140)
    t.fd(52)
    t.end_fill()
    t.rt(40)
    y = y - 32
t.penup()
t.goto(100, y)
t.pendown()
#thân cây
t.fillcolor("Brown")
t.begin_fill()
for i in range(0,2):
    if i == 0:
        t.fd(15)
    else:
        t.fd(30)
    t.rt(90)
    t.fd(91)
    t.rt(90)
t.fd(15)
t.end_fill()
#mặt trời
t.penup()
t.goto(100, 175)
t.pendown()
t.lt(90)
t.fd(45)
t.rt(90)
t.fd(100)
for i in range(0,10):
    t.backward(100)
    t.rt(45)
    t.fd(100)
t.backward(50)
t.lt(90)
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
