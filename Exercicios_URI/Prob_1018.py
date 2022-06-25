def counterBanknotes(value):
    banknotes, devolution = [0], lambda string, num: string[num:]
    if (len(value) > 2): banknotes[0] = int(value[:len(value)-2]); value = devolution(value, len(str(banknotes[0])))
    if (len(value) == 2):
      for k in range(2): banknotes += recursionCounter(int(value[k]), 0, [0, 0, 0])
    else: banknotes += [0, 0, 0] + recursionCounter(int(value[0]), 0, [0, 0, 0])
    return banknotes

def recursionCounter(n, i = 0, exit = [0, 0, 0]):
  check = (5, 2, 1)
  if n <= 0: return exit
  else:
    if n >= check[i]: exit[i]+= 1; return recursionCounter(n-check[i], i, exit)
    else: return recursionCounter(n, i+1, exit)

ent, notes = input(), ['100,00', '50,00', '20,00', '10,00', '5,00', '2,00', '1,00']
exit = counterBanknotes(ent)
print(ent)
for i in range(len(exit)):
  print('{} nota(s) de R$ {}'.format(exit[i], notes[i]))