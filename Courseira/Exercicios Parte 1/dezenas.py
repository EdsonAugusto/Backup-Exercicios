n=input('Digite um número inteiro:')
g=int(len(n))
if(g>=2):
    print('O dígito das dezenas é {}'.format(n[g-2]))
else:
    print('O dígito das dezenas é 0')