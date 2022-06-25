# Cifra de Cesar
from string import ascii_lowercase

def Cifrador(ent, string, alf = list(ascii_lowercase)):
      dic, cif, said = {' ': ' '}, alf[ent:] + alf[:ent], ''
      for i, chav in enumerate(alf):
          dic[chav] = cif[i]
      for k in string:
    	said += dic[k]
      print(dic)
      return said

def Conversor(string):
  st = []
  string.lower()
  for i in range(len(string)):
    st.append(string[i])
  return st
    
def main():
  import replit
  print('Cifra de Cesar')
  print('[1] Cifra [2] Decifrar [0] Sair')
  menu = True
  while menu:
    try:
      ent = int(input())
    except ValueError: print('\nEntrada incorreta, tente novamente.\n')
    else:
      if ent < 0 or ent > 2: print('\nEntrada incorreta, tente novamente.\n')
      else:
        replit.clear()
        return ent
  
    
#print(Conversor('test'))
print(Cifrador(18, Conversor('teste')))
print()