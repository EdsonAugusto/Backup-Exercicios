def remove_repetidos(l):
    if(len(l)>1):
        i=0
        while(i<=len(l)-1):
            k=0
            while(k<=len(l)-1):
                if(i!=k):
                    if(l[i]==l[k]):
                        del l[k]
                        i=0
                    else:
                        k+=1
                else:
                    k+=1
            i+=1
        return sorted(l)


#lis=[1,2,1,4,4.4,7,0,1]
#print(remove_repetidos(lis))