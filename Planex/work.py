import tkinter
import random


class minhaApp_tk (tkinter.Tk):
    # Tkinter.tk é a classe base para a janela padrão. A nossa classe minhaApp_tk irá herdar todas as funcionalidades da classe padrão.

    def __init__(self, parent):
        tkinter.Tk.__init__ (self, parent)
        # no construtor da nossa classe, apenas chamamo o construtor da classe pai, Tkinter.Tk.__init__()).
        self.parent = parent
        # geralmente necessitaremos  de acessar o pai de um objeto. É uma boa técnica  sempre salvar uma referencia ao pai.
        self.initialize ()
        # no método initialize criamos os demais objetos que serão apresentados na tela, inicializamos as variáveis globais (irc..),
        # inicializamos o hardware caso necessário, etc..

    def initialize(self):  # aqui criamos os widgets que serão apresentados na tela
        self.grid ()  # vamos dispor os objetos na tela dentro de uma grade
        self.lblC = tkinter.Label (self, text="Graus Centígrados")  # este objeto irá apresentar o primeiro número
        self.lblC.grid (column=0, row=0)  # nesta posição

        self.lblSep = tkinter.Label (self, text="<-->")  # este objeto irá apresentar o segundo  número
        self.lblSep.grid (column=1, row=0)  # nesta posição

        self.lblF = tkinter.Label (self, text="Graus Fahrenheit")  # este objeto irá apresentar o terceiro número
        self.lblF.grid (column=2, row=0)  # nesta posição

        self.entryC = tkinter.Entry (self)  # criamos o campo de texto onde está disponível o valor em gras centígrados
        self.entryC.grid (column=0, row=1,
                          sticky='EW')  # deixamos na posição correspondente a primeira coluna, segunda linha

        self.entryF = tkinter.Entry (self)  # criamos o campo de texto onde esta disponivel o valor em graus fahrenheit
        self.entryF.grid (column=2, row=1,
                          sticky='EW')  # deixamos na posição correspondente à terceira coluna, segunda linha

        self.btnCalculaF = tkinter.Button (self, text=u"Centígrado -> Fahrenheit",
                                           command=self.OnButtonCalculaFClick)  # criamos o objeto botão
        self.btnCalculaF.grid (column=0, row=3)  # e o colocamos na posição coluna 0, linha 3
        # associamos o clicar do botão ao método OnButtonCalculaFClick

        self.btnCalculaC = tkinter.Button (self, text=u" Fahrenheit -> Centígrado",
                                           command=self.OnButtonCalculaCClick)  # criamos o objeto botão
        self.btnCalculaC.grid (column=2, row=3)  # e o colocamos na posição coluna 0, linha 3
        # associamos o clicar do botão ao método OnButtonCalculaFClick

    def OnButtonCalculaFClick(self):  # calcula o valor em fahrenheit e mostra no campo correto
        fCent = float (self.entryC.get ())  # le o valor no campo de entrada de centígrados
        fFar = (9.0 * fCent) / 5 + 32.0  # calcula o novo valor
        self.entryF.delete (0, tkinter.END)  # apaga o campo destino
        self.entryF.insert (0, str (fFar))  # atualiza o campo destino com o novo valor

    def OnButtonCalculaCClick(self):  # calcula o valor em centígrados e mostra no campo correto
        fFar = float (self.entryF.get ())  # le o valor no campo de entrada de far
        fCent = (fFar - 32.0) * 5.0 / 9.0  # calcula o novo valor
        self.entryC.delete (0, tkinter.END)  # apaga o campo destino
        self.entryC.insert (0, str (fCent))  # atualiza o campo destino com o novo valor


# este é ponto onde o programa se inicia
# se o programa foi chamado a partir do interpretador python, o _name_  automaticamente será "__main__"

if __name__ == "__main__":
    app = minhaApp_tk (None)  # criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title ('Conversor C<->F')  # especificamos o título de nossa aplicação
    app.mainloop ()  # o programa entra no loop de espera de eventos (pressionar de menus, botões, etc..)

