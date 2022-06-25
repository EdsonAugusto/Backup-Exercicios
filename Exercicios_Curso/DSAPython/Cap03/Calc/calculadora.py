def mainCalculadora (ent = [], inf = ['primeiro', 'segundo']):
    print('Selecione numero da operação desejada:\n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão\n')
    ent.append(int(input('Digite sua opção (1/2/3/4): ')))
    print('\n')
    for i in range(2): ent.append('Digite o {} numero d% valor'%inf[i])
    

mainCalculadora()