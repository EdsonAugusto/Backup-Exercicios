def conta_vogais(palavras):
    vog=['A','a','E','e','I','i','O','o','U','u']
    acum=0
    for i in range(len(palavras)):
        for l in range(len(palavras[i])):
            for k in range(len(vog)):
                if(palavras[i][l]==vog[k]):
                    acum+=1
    return acum

def conta_letras(frase,contar='vogais'):
    assert contar != 'vogais' or contar != 'consoantes'
    palavras=frase.strip()
    if(contar=='vogais'):
        return conta_vogais(palavras)
    else:
        acum=0
        vog=conta_vogais(palavras)
        for i in range(len(palavras)):
            acum+=len(palavras[i].strip())
        return acum-vog


#print(conta_letras('programamos em python','consoantes'))