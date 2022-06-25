from tkinter import *

class Application:
    def __init__(self,master=None):
        self.widget1=Frame(master)
        self.widget1.pack()
        self.widget1['bg']='green'
        self.msg=Label(self.widget1,text='Test')
        self.msg['font']=('Arial','10')
        self.msg['bg']='green'
        self.msg.pack()
        self.sair=Button(self.widget1)
        self.sair['text']='sair'
        self.sair['font']=('Arial','10','bold')
        self.sair['bg']='yellow'
        self.sair['fg']=('black')
        self.sair['width']=30
        self.sair['command']=self.widget1.quit()
        self.sair.pack()

root=Tk()
Application(root)
root.mainloop()