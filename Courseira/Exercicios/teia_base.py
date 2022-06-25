from turtle import *

janela=Screen()
janela.setup(width=1200,height=600,startx=None,starty=None)
janela.title('A Teia')

traco=Turtle()
traco.pen(pencolor='red',pensize=3,fillcolor='black')
traco.speed(0)

def base(tam=-20,cir=-180,ang=-135,dis=40,test=None):
    if(test!=None):
        traco.pu()
        traco.setposition()
        traco.pd()
    pos=[]
    for i in range(8):
        traco.pu()
        traco.circle(tam,((cir/2)/2))
        pos.append(traco.position())
        traco.pd()
        traco.circle(tam,(cir/2))
        pos.append(traco.position())
        traco.pu()
        traco.circle(tam,(cir/2)/2)
        traco.right(ang)
    traco.right(-45)
    traco.fd(dis)
    traco.pd()
    return pos

c=base(-15,-180)
traco.right(30)
base(-30,-180,-135,80)
traco.right(30)
base(-60,-180,-135,160)#
traco.right(30)
base(-120,-180,-135,320)
traco.right(30)
base(-240,-180,-135)

traco.right(20)
traco.pu()
traco.setposition(c[0])
traco.pd()
traco.fd(200)

janela.exitonclick()