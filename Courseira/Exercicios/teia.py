from turtle import *

janela=Screen()
janela.bgcolor('black')

objeto=Turtle()
objeto.color('red','gray')
#objeto.shape('')
objeto.pensize(2)
objeto.speed(0)

def base():
    arq_pos1=[]
    arq_pos2=[]
    arq_pos3=[]
    pos=objeto.position()
    for i in range(8):
        objeto.left(90)
        objeto.fd(100)
        arq_pos1.append(objeto.position())
        objeto.fd(100)
        arq_pos2.append(objeto.position())
        objeto.fd(100)
        arq_pos3.append(objeto.position())
        objeto.right(135)
        if(i<=6):
            objeto.setposition(pos)
    return arq_pos1,arq_pos2,arq_pos3,pos

def forma(arq,pos,tam=170,ang=50):
    objeto.heading ()
    objeto.pensize(0)
    objeto.color('orange')
    for i in range(8):
        objeto.penup()
        objeto.setpos(arq[i])
        objeto.pendown()
        if(i<1):
            objeto.right(pos)
        if(i%2!=0):
            objeto.left(ang)
            objeto.circle(tam,85)
        else:
            objeto.left(ang)
            objeto.circle(-tam,-85)





a,b,c,pos=base()
posi=-240
forma(b,posi,100,60)
pos=-25
forma(c,pos)

janela.exitonclick()
