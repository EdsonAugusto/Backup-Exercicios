from turtle import *

janela=Screen()
janela.setup(width=1350,height=685,starty=0,startx=0)
janela.title('Praticas')

caneta=Turtle()
caneta.pen(pencolor='red',pensize=1,fillcolor='gray',speed=0)

caneta.pu()
caneta.setposition(-600,320)
caneta.pd()

def trov():
    caneta.color('red','yellow')
    caneta.fillcolor()
    ang=[-180,-130,-130]
    caneta.begin_fill()
    for i in range(3):
        caneta.towards(0,0)
        caneta.right(ang[i])
        caneta.fd(-25)
        caneta.right(130)
        if(i<2):
            caneta.fd(-60)
        else:
            caneta.fd(-60)
    caneta.right(-20)
    caneta.fd(40)
    caneta.right(-110)
    caneta.fd(25)
    caneta.right(-50)
    caneta.fd(-60)
    caneta.right(-130)
    caneta.fd(-25)
    caneta.right(-55)
    caneta.fd(78)
    caneta.end_fill()

trov()


janela.exitonclick()

#canto superior = -670,340