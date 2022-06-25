xent = input()
paran = list(map(float, ent.split()))
med = sum(paran) / len(paran)
if med >= 7:
    print('Media: {:.2f}'.format(med))
    print('Aluno aprovado.')
print(med)