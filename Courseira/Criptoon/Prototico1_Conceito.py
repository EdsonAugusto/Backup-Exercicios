def crip(n):
    alfa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    beta=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    delta=[0,1,2,3,4,5,6,7,8,9]
    rampage=[]
    omega=alfa+beta+delta
    cond=True
    while(cond):
        if(len(omega)>n):
            rampage.append(str(omega[n]))
            if(len(omega)>=n):
                del omega[n]
                cond=True
        if(len(omega)<n):
            n=0
            cond=True
        if(len(omega)<=0):
            break
    return rampage

print(crip(4))

