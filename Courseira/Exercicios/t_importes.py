from turtle import *
from logo import *

janela.bgcolor('black')

caneta=Turtle()
caneta.pen(pencolor='red',pensize=2,fillcolor='gray',speed=0)
caneta.pu()
caneta.setposition(-100,-300)
caneta.pd()

def marcacoes(objeto,dist,marc):
    '''Realiza a marcação de posição em uma determminada linha'''
    pos=[]
    while(dist>marc):
        objeto.fd(marc)
        dist-=marc
        pos.append(objeto.position())
    return pos

def poligono_reto(objeto,lados=2,alt=200,lg=200,ang=-90):
    '''Cria poligonos retos| Função de devolve 2 lados de um poligono em um chamada. | alt= Altura | lg= Largura | ang= Angulo'''
    for i in range(lados):
        objeto.fd(lg)
        objeto.right(ang)
        objeto.fd(alt)
        objeto.right(ang)

def poligono_inregular(objeto,lados=2,alt=180,larg=160,c_b=False,e_d=True):
    if(e_d==True):
        pos=[objeto.position()]
        alt,larg,ang=[80,-80],[160,-160],[-110,110]
        for i in range(lados):
            objeto.fd(larg[i])
            pos.append(objeto.position())
            objeto.right(ang[i])
            objeto.fd(alt[i])
            if(i<1):
                objeto.towards(0,0)
                objeto.right(110)
                objeto.pu()
                objeto.setposition(pos[1])
                objeto.pd()
            if(i>=1):
                objeto.right(-110)
                marcacoes(objeto,130,20)



caneta.color('red','white')
caneta.begin_fill()
poligono_reto(caneta,2,15,200,90)
pos=marcacoes(caneta,200,20)
caneta.setposition(pos[0])
caneta.end_fill()
poligono_inregular(caneta)
caneta.begin_fill()
caneta.right(180)
#poligono_reto(caneta,2,-10,134)
caneta.end_fill()



'''poligonos(caneta,2,10,20)
caneta.setposition(pos[1])
poligonos(caneta,2,10,20)'''
janela.exitonclick()
