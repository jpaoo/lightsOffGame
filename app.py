from foco import *

class Application(Frame):

    def __init__(self, master,x ,y):
        #super se utiliza para obtener los metodos del padre, en este caso el frame
        super(Application, self).__init__()
        self.master = master
        self.crear_focos(x, y)

    def crear_focos(self, y, x):
        for columna in range(x):
            Grid.rowconfigure(self, columna, weight=1)
            for fila in range(y):
                Grid.columnconfigure(self, fila, weight=1)
                btn = Foco()
                btn.grid(row=columna, column=fila, sticky=N + S + E + W)

