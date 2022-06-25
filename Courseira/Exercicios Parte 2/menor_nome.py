from re import *
def menor_nome(nomes):
    mNome=nomes[0].strip()
    for i in range(1,len(nomes)):
        nomes[i]=nomes[i].strip()
        if(len(mNome)>len(nomes[i])):
            mNome=nomes[i]
    return mNome.capitalize()

#print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))