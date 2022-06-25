import re

def le_assinatura():
#A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))


    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print()
    return textos

def separa_sentencas(texto):
#A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
#A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
#A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    return frase.split()

def n_palavras_unicas(lista_palavras):
#Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
#Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def remove_pont(text,strin):
    novo_text=text
    for i in strin:
        novo_text=novo_text.replace(i,' ')
    return novo_text

def retira_sentenca(texto):
    sentenca=re.split(r'[;,:.!?]+',texto)
    if(sentenca[-1]==''):
        del sentenca[-1]
    return sentenca

def retira_pont(sentenca):
    for i in range(len(sentenca)):
        sentenca[i]=re.split(r'[,:;.?!]+', sentenca[i])
        if(sentenca[i][-1]==''):
            del sentenca[i][-1]
        sentenca[i]=sentenca[i][0]
    return sentenca

def q_caracter(palavras):
    acum=0
    for i in range(len(palavras)):
        acum+=len(palavras[i])
    return acum

def m_caracter(text):
    nov_text=remove_pont(text,':;.,!?')
    sep=retira_pont(separa_palavras(nov_text))
    return q_caracter(sep)/len(sep)

def type_token(a,b):
    return a/b

def harpax(texto):
    return n_palavras_unicas(texto)/len(texto)

def m_sentenca(texto):
    return q_caracter(separa_sentencas(texto))/len(separa_sentencas(texto))

def m_frases(texto):
    return len(retira_sentenca(texto))/len(separa_sentencas(texto))

def c_sentenca(texto):
    acum=0
    texto=retira_sentenca(texto)
    for i in range(len(texto)):
        acum+=len(texto[i])
    return acum/len(texto)

def compara_assinatura(as_a, as_b):
#IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
    pass
    comp_a=0
    comp_b=0
    sim=[]
    for i in range(len(as_a)):
        comp_a=as_a[i]
        comp_b=as_b[i]
        if(comp_a>comp_b):
            sim.append((comp_a-comp_b)/ 6)
        else:
            sim.append((comp_b-comp_a)/6)
    acum=0
    for k in range(len(sim)):acum+=sim[k]
    return acum

def calcula_assinatura(texto):
#IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
    pass
    ind=[]
    c=separa_palavras(remove_pont(texto,',.;:!?'))
    x=len(c)
    y=n_palavras_diferentes(c)
    ind.append(m_caracter(texto))
    ind.append(type_token(y,x))
    ind.append(harpax(c))
    ind.append(m_sentenca(texto))
    ind.append(m_frases(texto))
    ind.append(c_sentenca(texto))
    return ind[0],ind[1],ind[2],ind[3],ind[4],ind[5]

def avalia_textos(textos, ass_cp):
#IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    pass
    cal_ass=[]
    grau_sim=[]
    for i in range(len(textos)):
        cal_ass.append(calcula_assinatura(textos[i]))
    for k in range(len(cal_ass)):
        grau_sim.append(compara_assinatura(cal_ass[i],ass_cp))
    n=0
    g=1
    while(n<=len(grau_sim)-1):
        if(grau_sim[n]>(grau_sim[g])):
            n+=1
        else:
            g=n
            n+=1
    return g

ass_ifect=le_assinatura()
print()
rec_textos=le_textos()
ava_text=avalia_textos(rec_textos,ass_ifect)
print()
print('O autor do texto ',ava_text,'está infectado com COH-PIAH')
'''
texto='NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
texto1='Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.'
print(calcula_assinatura(texto1))
#print(m_caracter(texto1))
#c=retira_pont(separa_palavras(texto1))
#print(m_caracter(texto1))
print(retira_sentenca(texto1))

print(compara_assinatura((4.34, 0.05, 0.02, 12.81, 2.16, 0.0),(3.96, 0.05, 0.02, 22.22, 3.41, 0.0)))
'''
