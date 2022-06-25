from math import *
def fatorial(a):
    return factorial(a)

def binomial(n,k):
    n1=fatorial(n)
    k=fatorial(k)*fatorial((n-k))
    return n1/k
print(binomial(5,3))