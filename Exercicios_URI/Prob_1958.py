inputValue = float(input())
verified = str(inputValue)
if verified[0] == '-': print('%.4E'%(inputValue))
else: print('+%.4E'%(inputValue))