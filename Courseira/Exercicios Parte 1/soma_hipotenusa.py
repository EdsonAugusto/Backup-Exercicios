def e_triangulo(c):
    a=1
    while(a<=c):
        b=1
        while(b<=a):
           if(a**2+b**2==c**2):
               return c
           else:
               b+=1
        a+=1
    return 0

def soma_hipotenusas(h):
    i=1
    c=0
    while(i<=h):
        c+=e_triangulo(i)
        i+=1
    return c

print(soma_hipotenusas(3900))