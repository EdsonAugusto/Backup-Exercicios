def tupla_par(t):
  tup = []
  for i in range(len(t)):
    if (i % 2) == 0:
      tup.append(t[i])
  return tuple(tup)
