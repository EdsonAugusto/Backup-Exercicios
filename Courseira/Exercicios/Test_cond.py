#from pytest import mark
while True:
    try:
        n=input ()
        c=n.split(' ')
        var=(int(c[0])*int(c[1]))*2
        print(var)
    except EOFError:
        break



"""@mark.parametrize('entrada, saida',[
    ('16 40',24),
    ('64 21',43),
    ('44 48',4),
    ('30 17',13),
    ('67 51',16),
    ('12 11',1),
    ('4 23',19),
    ('41 32',9),
    ('41 58',17),
    ('1 40',39),
    ('13 49',36),
    ('48 83',35),
    ('5 75',70),
    ('16 100',84),
    ('58 72',14),
    ('70 99',29),
    ('2 39',37),
    ('18 75',57),
    ('16 37',21),
    ('88 43',45),
    ('57 23',34)
])
def test_dif(entrada,saida):
    dif(entrada)==saida"""