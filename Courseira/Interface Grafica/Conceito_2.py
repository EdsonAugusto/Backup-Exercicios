from tkinter import *

class Application:
    def __init__(self,master=None):
        self.fontePadrao=('Arial','10')
        self.primeiroContainer=Frame(master)
        self.primeiroContainer['pady']=10
        self.primeiroContainer.pack()

        self.segundoContainer=Frame(master)
        self.segundoContainer['pady']=20
        self.segundoContainer.pack()

        self.terceiroContainer=Frame(master)
        self.terceiroContainer['pady']=20
        self.terceiroContainer.pack()

        self.quartoContainer=Frame(master)
        self.quartoContainer['pady']=20
        self.quartoContainer.pack()

        self.titulo=Label(self.primeiroContainer,text='Dados do Usuario')
        self.titulo['font']=('Arial','10')
        self.titulo.pack()

        self.nomeLabel=Label(self.segundoContainer,text='Nome',font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome=Entry(self.segundoContainer)
        self.nome['width']=30
        self.nome['font']=self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senha=Label(self.terceiroContainer,text='Senha',font=self.fontePadrao)
        self.senha.pack(side=LEFT)

        self.senha=Entry(self.terceiroContainer)
        self.senha['width']=30
        self.senha['font']=self.fontePadrao
        self.senha['show']='*'
        self.senha.pack(side=LEFT)

        self.auteticar=Button(self.quartoContainer)
        self.auteticar['text']='Autenticar'
        self.auteticar['font']=self.fontePadrao
        self.auteticar['width']=12
        self.auteticar['command']=self.verificaSenha
        self.auteticar.pack()

        self.mensagem=Label(self.quartoContainer,text=' ',font=self.fontePadrao)
        self.mensagem.pack()

    def verificaSenha(self):
        usuario=self.nome.get()
        senha=self.senha.get()
        if(usuario=='ed') and(senha=='ed'):
            self.mensagem['text']='Autenticado'
        else:
            self.mensagem['text']='Erro na autenticação'

root=Tk()
Application(root)
root.mainloop()