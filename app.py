from foco import *

class Application(Frame):

    mis_focos = []

    def __init__(self, master, x, y):
        #super se utiliza para obtener los metodos del padre, en este caso el frame
        super(Application, self).__init__()
        self.intentos = 0
        self.master = master
        self.crear_focos(x, y)
        self.encendidos = 0

    def crear_focos(self, y, x):
        i = 1
        for columna in range(x):
            Grid.rowconfigure(self, columna, weight=1)
            for fila in range(y):
                Grid.columnconfigure(self, fila, weight=1)
                btn = Foco(i)
                btn.setCol(fila)
                btn.setFil(columna)
                i = i + 1
                self.mis_focos.append(btn)
                btn.grid(row=columna, column=fila, sticky=N + S + E + W)
        print("Hay:", len(self.mis_focos), "focos en total")
        self.totalOn()
        print("Llevas:", self.intentos, "intentos")

    def getFocos(self):
        return self.mis_focos

    def getIntentos(self):
        return self.intentos

    def setIntentos(self, n):
        self.intentos = self.intentos + n

    def totalOn(self):
        counter = 0
        for i in self.mis_focos:
            if(i.getOn()):
                counter = counter + 1
        self.encendidos = counter
        print("Hay:", self.encendidos, "prendidos.")

    def finJuego(self):
        if self.encendidos == 0:
            print("Ganaste! Te tomo:", self.getIntentos(), "intentos.")
