def obter_mais_longa_substring(s):
  string, i, lis = '', 0, []
  while i < (len(s)-1):
    if s[i] <= s[i+1]:
      string += s[i:i+1]
      i += 1
    else:
      string += s[i]
      lis.append(string)
      string = ''
      i += 1
  maior = ''
  for i in range(len(lis)):
    if len(lis[i]) > len(maior):
      maior = lis[i]
  return maior

print(obter_mais_longa_substring('python'))