def elefantes(n,temp=None):
    if(temp==None):temp=n
    if(n<1):
        return ''
    if(n==1):
        return 'Um elefante incomoda muita gente\n'
    else:
        if(n>=temp):
            return elefantes(n-1,temp) + str(n) + ' elefantes' + incomodam(n) + ' muito mais\n'
        else:
            return elefantes(n-1,temp)+str(n)+' elefantes'+incomodam(n)+' muito mais\n'+str(n)+' elefantes incomodam muita gente\n'

def incomodam(n):
    return ' incomodam'*n







