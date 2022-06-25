ent_time=[]
import time
import os

def time_res(h,m,s):
    if (h>23):
        h=0
    else:
        if (m>59):
           m=0
        else:
            if (s>=59):
                s=0

def relogio(h,m,s):
    while h<=23:
        while m<=60:
            while s<=60:
                #print('{}:{}:{}'.format(h,m,s))
                print('%s:%s:%s'%(reg_menor(h),reg_menor(m),reg_menor(s)))
                time.sleep(1)
                s=s+1

                if (s>=59):
                    m=m+1
                    s=0
                    time_res(h,m,s)
                    os.system('cls')
                if (m>59):
                    m=0
                    h=h+1
                    os.system('cls')
                if (h>23):
                    h=0
                    os.system('cls')

def reg_menor(a):
    g=0
    if a < 10:
        g=a
        h=0
        str(h)
        str(g)
        return str(h)+str(g)
    else:
        return a

def ent_res():
    paramentro=['Horas: [0 a 23]','Minutos: [0 a 59]']
    verif=[23,59]
    i=0
    c=1
    while (i<=1) and (c<=2):
        cont=True
        while (cont==True):
            ent_time.append(int(input(paramentro[i:c])))
            if ent_time[i:c]<verif[i:c]:
                i=i+1
                c=c+1
                cont=False
            elif ent_time[i:c] > verif[i:c]:
                del(ent_time[i:c])
                print('Erro: paramentros invalidos')

ent_res()
ent_time.append(0)
relogio(ent_time[0],ent_time[1],ent_time[2])