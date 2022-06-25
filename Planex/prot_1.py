from tkinter import *

class App:
    def __init__(self,master=None):
        
        pass


root=Tk()
root.title('Planex')
cima,baixo=(root.winfo_screenwidth()),(root.winfo_screenheight())
root.geometry('%dx%d+0+0'%(cima-18,baixo-80))
App(root)
root.mainloop()