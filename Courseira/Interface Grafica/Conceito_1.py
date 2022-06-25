from tkinter import *

class App_Calc:
    def __init__(self,master=None):
        self.widged_app_calc=Frame(master)
        self.widged_app_calc.pack()
        self.widged_app_calc['bg']='grey'
        self.widged_app_calc['width']=800
        self.msg=Label(self.widged_app_calc,text='Calculadora Avançanda')
        self.msg['font']=('Comic Sans','10')
        self.msg.pack()

        self.sair = Button(self.widged_app_calc)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widged_app_calc.quit
        self.sair.pack()


root=Tk()
root.geometry('800x600')

App_Calc(root)
root.mainloop()