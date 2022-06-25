import re
def retira_pont(sentenca):
    for i in range(len(sentenca)):
        sentenca[i]=re.split(r'[,:;.?!]+', sentenca[i])
        if(sentenca[i][-1]==''):
            del sentenca[i][-1]
        sentenca[i]=sentenca[i][0]
    return sentenca

texto=['Muito', 'além,', 'nos', 'confins', 'inexplorados', 'da', 'região', 'mais', 'brega', 'da', 'Borda', 'Ocidental', 'desta', 'Galáxia,', 'há', 'um', 'pequeno', 'sol', 'amarelo', 'e', 'esquecido.', 'Girando', 'em', 'torno', 'deste', 'sol,', 'a', 'uma', 'distancia', 'de', 'cerca', 'de', '148', 'milhões', 'de', 'quilômetros,', 'há', 'um', 'planetinha', 'verde-azulado', 'absolutamente', 'insignificante,', 'cujas', 'formas', 'de', 'vida,', 'descendentes', 'de', 'primatas,', 'são', 'tão', 'extraordinariamente', 'primitivas', 'que', 'ainda', 'acham', 'que', 'relógios', 'digitais', 'são', 'uma', 'grande', 'ideia.']
print(retira_pont(texto))

texto='Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia.'
'''
ind=[]
c=retira_pont(separa_palavras(texto))
x=len(c)
y=n_palavras_diferentes(c)
ind.append(m_caracter(c))
ind.append(type_token(y,x))
ind.append(harpax(c))
ind.append(m_sentenca(texto))
ind.append(m_frases(texto))
ind.append(len(retira_sentenca(texto)))
ind.append(c_sentenca(texto))
print(ind)
'''
print(calcula_assinatura(texto))
#print(compara_assinatura(ind,ind))