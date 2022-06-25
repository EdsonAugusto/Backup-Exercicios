def sao_multiplicaveis(m1,m2):
    if(len(m1)>1 and len(m2)>1):
        if(len(m1[0])==len(m2))or(len(m1)==len(m2[0]))or(len(m1)==len(m2)):
            for i in range(len(m1)):
                if(len(m1[i])!=1)and(len(m2[i])!=1)or(m1[i]==m2[i]):
                    return False
            return True
        else:
            return False
    else:
        return True

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
'''

m1 = [[1],[1],[1]]
m2 = [[2]]

'''
print(sao_multiplicaveis(m1,m2))
print(len(m1))
print(len(m2))


