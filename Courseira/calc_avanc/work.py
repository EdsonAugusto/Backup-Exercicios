from tkinter import *

'''
root=Tk()
root.title('Calculadora Cientifica Avançada')
#root.configure(background='black')
root.geometry('500x500')

image=PhotoImage(file='back.png')
image=image.subsample(1,1)

labelimage=Label(image=image)
labelimage.place(x=0,y=0,relwidth=1.0,relheight=1.0)
'''
class Application:

    def __init__(self,master=None):
        self.fontePadrao=('Arial','10','italic')
        self.calc_avanc=Frame(master)
        #self.calc_avanc['bg']='-transparentcolor'
        self.calc_avanc.pack()

        self.tit=Label(self.calc_avanc,text='Calculadora Cientifica Avançada')
        self.tit['font']='Old English Text MT','15','italic','bold'
        #self.tit['bg']=''
        self.tit.pack()

        self.subtit=Label(text='<>Escolha área de cálculo<>')
        self.subtit['font'] = 'Bradley Hand ITC', '15', 'italic','bold'
        self.subtit['fg']='black'
        self.subtit.pack()

        self.bot_Fisica=Button(master)
        imagem_fis=PhotoImage(file='fis_bot.png')
        self.bot_Fisica.config(image=imagem_fis)
        self.bot_Fisica.imagem=imagem_fis
        self.bot_Fisica.imagem['width']=200
        self.bot_Fisica.imagem['height']=100
        self.bot_Fisica.imagem['command']=Fis_menu
        self.bot_Fisica.place(x=40,y=150)

        self.bot_Matematica=Button(master)
        imagem_mat=PhotoImage(file='mat_bot.png')
        self.bot_Matematica.config(image=imagem_mat)
        self.bot_Matematica.imagem=imagem_mat
        self.bot_Matematica.imagem['width']=200
        self.bot_Matematica.imagem['height']=100
        self.bot_Matematica.place(x=280,y=150)

        self.bot_Quimica=Button(master)
        imagem_qui=PhotoImage(file='')
        self.bot_Quimica.config(image=imagem_qui)
        self.bot_Quimica.imagem=imagem_qui
        self.bot_Quimica.imagem['width']=200
        self.bot_Quimica.imagem['height']=100
        self.bot_Quimica.place(x=520,y=150)

        self.bot_Outros=Button(master)
        imagem_out=PhotoImage(file='')
        self.bot_Outros.config(image=imagem_out)
        self.bot_Outros.imagem=imagem_out
        self.bot_Outros.imagem['width']=200
        self.bot_Outros.imagem['height']=100
        self.bot_Outros.place(x=160,y=280)

        self.bot_Credito=Button(master)
        imagem_cre=PhotoImage(file='')
        self.bot_Credito.config(image=imagem_cre)
        self.bot_Credito.imagem=imagem_cre
        self.bot_Credito.imagem['width']=200
        self.bot_Credito.imagem['height']=100
        self.bot_Credito.place(x=420,y=280)


root=Tk()
root.title('Calculadora Cientifica Avançada')

root.geometry('767x459')

image=PhotoImage(file='back.png')
image=image.subsample(1,1)

labelimage=Label(image=image)
labelimage.place(x=0,y=0,relwidth=1.0,relheight=1.0)
root.wm_attributes('-transparentcolor', 'white')
#c=Checkbutton(root, indicatoron=False, image=img_off,selectimage=img_on, bd=0, selectcolor='', width=12, height=12)
#c.pack(padx=100,pady=100)

Application(root)
root.mainloop()
