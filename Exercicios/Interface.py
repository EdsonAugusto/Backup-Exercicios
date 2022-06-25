import turtle
wn = turtle.Screen()             # Cria uma janela e define seus atributos
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # cria tess e define seus atributos
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()           # cria alex

tess.forward(80)                 # tess desenha um triângulo equilátero
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete o triângulo

tess.right(180)                  # tess muda de direção
tess.forward(80)                 # tess se move para longe da origem

alex.forward(50)                 # alex desenha um quadrado
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.back(50)
alex.right(180)
alex.circle(360,60,60)

wn.exitonclick()

