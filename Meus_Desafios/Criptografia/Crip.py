from string import ascii_letters

class Criptografia:

    def __init__(self, string, chave, dec = None, alf_letters = None, crip = None, said = None):
        self.string = string
        self.chave = chave
        self.dec = dec
        self.alf_letters = alf_letters
        self.crip = crip
        self.said = said
        

    def slicer(self, string):
        lis = []
        for i in range(len(string)):
            lis.append(string[i])
        return lis

    def encriptador(self):
        pass

    def cifra(self):
        pass

    def decifrador(self):
        pass

class Cifra_Cesar(self, ):
    
    def __init__(self, string, chave, dec = False, alf_letters = list(ascii_letters), crip = {' ':' '}, said = ''):
        super().__init__(string, chave-1, dec, alf_letters, crip, said)

    def encriptador(self):
        alf_conv = self.alf_letters[self.chave:] + self.alf_letters[:self.chave]
        for i, key in enumerate(self.alf_letters): 
            self.crip[key] = alf_conv[i]
        self.string = super().slicer(self.string)
        for i in self.string:
            self.said += self.crip[i]
        return self.said

    def decifrador(self):
        self.Cifra_Cesar(self.string, self.chave)
        return self.encriptador()

    
'''
    def cifra(self, chave=None):
        self.crip, chave = self.encriptador(), self
        '''
        




cif = Criptografia.Cifra_Cesar('t', 5)
print(cif.encriptador())
print(cif.decifrador())

#print(cif.decifrador())