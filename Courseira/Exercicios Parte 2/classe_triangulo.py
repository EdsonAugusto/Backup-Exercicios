class Triangulo:
    def __init__(self,lado_a,lado_b,lado_c):
        self.a=lado_a
        self.b=lado_b
        self.c=lado_c

    def a(self):
        print(self.a)
        return self.a

    def b(self):
        print(self.b)
        return self.b

    def c(self):
        print(lado_c)
        return self.c

    def perimetro(self):
        print(self.a+self.b+self.c)
        return self.a+self.b+self.c

    def tipo_lado(self):
        if(self.a==self.b)and(self.a==self.c):
            print('equilátero')
            return 'equilátero'
        elif(self.a==self.b)or(self.a==self.c)or(self.b==self.c):
            print('isósceles')
            return 'isósceles'
        else:
            print('escaleno')
            return 'escaleno'

    def retangulo(self):
        if(self.a**2+self.b**2==self.c**2)or(self.a**2+self.c**2==self.b**2)or(self.b**2+self.c**2==self.a**2):
            print('True')
            return True
        else:
            print('False')
            return False

    def semelhantes(self,tr):
        t1=[self.a,self.b,self.c]
        t2=[tr.a,tr.b,tr.c]
        t1.sort()
        t2.sort()
        if(t1[0]>t2[0]):
            if(t1[0]%t2[0]==0)and(t1[1]%t2[1]==0)and(t1[2]%t2[2]==0):
                print('True')
                return True
            else:
                print('False')
                return False
        else:
            if(t2[0]%t1[0]==0)and(t2[1]%t1[1]==0)and(t2[2]%t1[2]==0):
                print('True')
                return True
            else:
                print('False')
                return False
