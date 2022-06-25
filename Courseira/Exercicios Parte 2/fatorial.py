def fatorial(n):
    if(n<1):
        return 1
    else:
        return n*fatorial(n-1)

from pytest import mark
@mark.parametrize('entrada, saida',[
                (1,1),
                (2,2),
                (3,6),
                (4,24),
                (5,120)
                ])
def test_fatorial(entrada,saida):
    fatorial(entrada)==saida