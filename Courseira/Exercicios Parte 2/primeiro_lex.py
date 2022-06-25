def primeiro_lex(list):
    p_lex=list[0]
    for i in range(1,len(list)):
        if(ord(p_lex[0])!=(ord(list[i][0]))):
            if (ord(p_lex[0])>(ord(list[i][0]))):
                p_lex=list[i]
        else:
            for k in range(len(list[i])):
                if (ord(p_lex[0])!=(ord(list[i][k]))):
                    break
            if(ord(p_lex[0])>ord(list[i][k])):
                p_lex=list[i]
    return p_lex

#print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))