from foco import *
import random

class Application(Frame):

    mis_focos = []
    intentos = 0

    def __init__(self, master, x, y, dif, intent):
        #super se utiliza para obtener los metodos del padre, en este caso el frame
        super(Application, self).__init__()
        self.intentos = intent
        self.master = master
        self.encendidos = 0
        self.dificultad = dif
        self.crear_focos(x, y)

    def crear_focos(self, y, x):
        i = 1
        for columna in range(x):
            Grid.rowconfigure(self, columna, weight=1)
            for fila in range(y):
                Grid.columnconfigure(self, fila, weight=1)
                btn = Foco(i)
                btn.setCol(fila)
                btn.setFil(columna)
                #Enciende el foco de manera aleatoria segun el nivel de dificultad
                rand = random.randrange(0, 100)
                if self.dificultad == 1 and rand <= 10 or i == 2:
                    btn.cambiacolor()
                elif self.dificultad == 2 and rand <= 30 or i == 2:
                    btn.cambiacolor()
                elif self.dificultad == 3 and rand <= 50 or i == 2:
                    btn.cambiacolor()
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
            print("Ganaste! Te tomo:", self.intentos, "intentos.")
            cantFocos = len(self.mis_focos)
            totalIntentos = self.intentos

            if totalIntentos <= cantFocos/2:
                print("Eres todo un experto! Intenta jugar con más focos.")
            elif totalIntentos < cantFocos:
                print("Tu nivel es avanzado, te falta poco para ser un maestro!")
            else:
                print("Eres un novato, sigue practicando")
            quit()

