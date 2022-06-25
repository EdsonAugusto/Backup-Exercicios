def vogal(v):
    vog=['a','A','e','E','i','I','o','O','u','U']
    cond=False
    i=0
    while(cond)or(i<=9):
        cond=(v==vog[i])
        i+=1
        if(cond):
            return cond
    return cond
a=input('Letra: ')
print(vogal(a))