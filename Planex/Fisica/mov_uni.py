import turtle

janela = turtle.Screen()
janela.bgcolor('black')

def tab(obj, ang):
    pass


def a(obj, tam = 100):
    obj.fd(tam//2)
    return obj.circle(-tam,45)

def organizador(obj, ang, pos):
    obj.pu()
    obj.setpos(pos)
    obj.pd()
    obj.rt(ang)

def basicSlice(obj, size, slice, types = True, interval = None):
    #size = tamanho da forma
    #slice = quantidade de fatias
    #interval = tamanho do intervalo da fatia definido ou vazio *None que é automatico
    #types = reta *True, circulo = *False
    if interval == None:
        if types:
            hidden = size//slice
            for i in range(slice):
                obj.pd()
                obj.fd(hidden)
                obj.pu()
                obj.fd(hidden)

def frascoAmostra(obj):
    lis = [obj.pos()]
    for i in range(2):
        if i < 1:
            obj.circle(60,-45)
            lis.append(obj.pos())
        else:
            organizador(obj, -45, lis[0])
            obj.fd(20)
            obj.circle(60,45)
            lis.append(obj.pos())
    #del lis[0]
    for k in range(1,len(lis)):
        organizador(obj, -90, lis[k])
        obj.circle(-60, 100)
    #organizador(obj, -15, lis[2])
    #obj.circle(60, 100)

    return lis


pen = [turtle.Turtle(), turtle.Turtle()]
pen[0].color('green')

'''
pen[0].pu()
pen[0].setpos(-650,340)
pen[0].pd()
'''

#frascoAmostra(pen[0])
basicSlice(pen[0],400,4)

janela.exitonclick()