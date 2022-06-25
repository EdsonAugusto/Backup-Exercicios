'''def matrixElementsSum(matrix):
    soma=0
    for i in range(len(matrix)-1):
        for k in range(len(matrix[i])):
            if(i<=0):
                soma+=matrix[i][k]
            else:
                if(matrix[i][k]!=0)and(matrix[i-1][k]!=0):
                    soma+=matrix[i][k]+matrix[i+1][k]
    return soma'''
'''
lis=[[1,0,0,0],[0,2,0,0],[0,0,3,0]]

m= list(zip(*lis))
print(m)'''
def newRoadSystem(roadRegister):
    comp=list(zip(*roadRegister))
    said=[]*(len(comp)-1)
    for k in range(len(comp)):
        temp = False
        for j in range(len(comp[k])):
            temp = temp or comp[k][j]
        said[k][k].append(temp)
    fin=0
    for i in range(len(said)):
        if(said[i][l]==True):
            fin+=1
    print(said)
    if(fin==len(roadRegister))or(fin==0):
        return True
    else:
        return False

false=False
true=True

l=[[false,true,false],
 [false,false,false],
 [true,false,false]]
print(newRoadSystem(l))

