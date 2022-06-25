def numero_perfeito(n):
  lis = []
  for i in range(1, (n//2)+1):
    if (n % i) == 0:
      lis.append(i)
  return sum(lis) == n