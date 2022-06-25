
def mix(s1, s2):
    lis_a, lis_b = contLetra(s1), contLetra(s2)

    return lis_a, lis_b

def contLetra(s):
    s, string = s.split(' '), {}
    for i in range(len(s)):
        for k in range(len(s[i])):
            if s[i][k] in string: string[s[i][k]] += 1
            else: string[s[i][k]] = 1
    return string

def classificador(dic1, dic2):
    keys1, keys2 = list(dic1.keys()), list(dic2.keys())
    while (len(dic1) >= 1) or (len(dic2) >= 1):
        if len(dic1) >= len(dic2):
            for i in range(len(keys1)):
                if max(dic) >  
                

print(mix("Are they here", "yes, they are here"))