def soma_matrizes(m1,m2):
    if(len(m1)==len(m2)):
        if(len(m1)>1):
            for i in range(len(m1)):
                for l in range(len(m1[i])):
                    if(len(m1[i])!=len(m2[i])):
                        return False
        else:
            return [[m1[0][0]+m2[0][0]]]
        m3=[]
        for i in range(len(m1)):
            m3.append([])
            for l in range(len(m1[i])):
                m3[i].append(m1[i][l]+m2[i][l])
        return m3
    else:
        return False
#m1 = [[1]]
#m2 = [[2]]
#print(soma_matrizes(m1,m2))