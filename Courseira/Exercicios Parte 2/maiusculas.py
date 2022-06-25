from re import *
def maiusculas(frase):
    palavras=frase.split()
    letrasM=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ocorrencias=['']
    for i in range(len(palavras)):
        for l in range(len(palavras[i])):
            for k in range(len(letrasM)):
                if(palavras[i][l]==letrasM[k]):
                    ocorrencias[0]+=(palavras[i][l])
    return ocorrencias[0]

print(maiusculas('HELLO WORLD'))

