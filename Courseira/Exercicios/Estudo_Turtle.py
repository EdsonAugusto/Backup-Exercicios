from turtle import *
janela=Screen()
janela.bgcolor('green')

objeto=Turtle()
#objeto.hideturtle() #Retira ponta
objeto.pensize(5) #Tamanho do traço
#objeto.color('white')
objeto.speed(5) #Velocidade

def mov():
    list=('black','white')
    paran=(90,-90)
    for i in range(len(list)):
        objeto.color(list[i],list[i])
        objeto.begin_fill ()#Abertura do traço com preechimento
        objeto.penup() #Lapis Desativado
        objeto.right(paran[i])
        objeto.fd(40)
        objeto.pendown() #Lapis Ativo
        objeto.circle(-10)
        objeto.end_fill()#Fechamento do traço com realizado apos o fechamento da forma
        if(i<1):
            objeto.penup()
            objeto.fd(-40)
            objeto.right(90)
            objeto.circle(100,-180)

def main():
    list=['white','black']
    for i in range(len(list)):
        objeto.color('black',list[i])
        objeto.begin_fill()
        if(i<1):
            objeto.circle(-50,-180)
            objeto.circle(50,-180)
            objeto.circle(100,-180)
        else:
            objeto.circle(100,-180)
            objeto.circle(50,180)
            objeto.circle(-50,180)
        objeto.end_fill()
    objeto.circle (-100, 180)
    mov()

main()

janela.exitonclick()