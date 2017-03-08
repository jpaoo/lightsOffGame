from foco import *

class Application(Frame):

    def __init__(self, master):
        #super se utiliza para obtener los metodos del padre, en este caso el frame
        super(Application, self).__init__()
        self.master = master
        self.crear_focos()
        #self.grid(row=0, column=0, sticky=N + S + E + W)

    def crear_focos(self):
        for row_index in range(10):
            Grid.rowconfigure(self, row_index, weight=1)
            for col_index in range(10):
                Grid.columnconfigure(self, col_index, weight=1)
                btn = Foco()
                #btn = Button(self)  # create a button inside frame
                btn.grid(row=row_index, column=col_index, sticky=N + S + E + W)

'''
    crea la cantidad de focos pasados en el parametro x, de momento no se utiliza (CAMBIAR)
    def crear_focos(self, x):
        focos = []
        for i in range(0,25):
            focos.append(Foco())
            focos[i].pack()

'''