import turtle

def draw_e():
    turt.fd(50)
    turt.bk(50)
    turt.right(90)
    turt.fd(50)
    turt.left(90)
    turt.fd(50)
    turt.bk(50)
    turt.right(90)
    turt.fd(50)
    turt.left(90)
    turt.fd(50)
def draw_m():
    turt.left(90)
    turt.forward(100)
    turt.right(160)
    turt.forward(100)
    turt.left(160)
    turt.forward(100)
    turt.right(160)
    turt.forward(100)
    turt.left(90)
def draw_i():
    turt.right(105)
    turt.forward(100)
    turt.bk(100)
    turt.penup()
    turt.bk(30)
    turt.pendown()
    turt.circle(10)
def draw_r():
    turt.fd(90)
    turt.circle(-35, 300)
    turt.left(150)
    turt.fd(80)

tur = turtle.Screen()
turt = turtle.Turtle()
tur.bgcolor("black")
turt.color("cyan")
turt.shape("turtle")
turt.pensize(10)

draw_e()

turt.penup()
turt.fd(30)
turt.pendown()

draw_m()

turt.penup()
turt.setpos(160,5)
turt.pendown()

draw_i()

turt.penup()
turt.fd(130)
turt.left(90)
turt.fd(35)
turt.left(90)
turt.pendown()

draw_r()
#:) çizimi
turt.penup()
turt.fd(60)
turt.pendown()
turt.circle(20)
turt.penup()
turt.left(50)
turt.fd(100)
turt.pendown()
turt.circle(20)
turt.penup()
turt.right(90)
turt.fd(30)
turt.pendown()
turt.circle(-40,180)

turtle.done()
