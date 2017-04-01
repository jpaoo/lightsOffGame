from tkinter import *
import app

class Foco(Button):

    def __init__(self, x, *args, **kwargs):
        Button.__init__(self, *args, **kwargs, command=self.botonPressed)
        self['bg'] = 'grey'
        self.num = x
        self.on = False
        self.fil = 0
        self.col = 0

    def botonPressed(self):
        #Encender/apagarse a si mismo
        self.cambiacolor()
        #print("Fil:", self.fil, "Col:", self.col)

        #Apagar vecino de la izquierda en la misma fila
        if (app.Application.mis_focos[self.num - 2].getFil() == app.Application.mis_focos[self.num-1].getFil()):
            app.Application.mis_focos[self.num - 2].cambiacolor()
        #Comprobar que el vecino de la derecha exista
        if(self.num >= len(app.Application.mis_focos)):
            print("No se hace nada, fuera de rango")
        else:
            #Si existe el vecino y está en la misma fila, apagarlo/encenderlo
            if(app.Application.mis_focos[self.num - 1].getFil() == app.Application.mis_focos[self.num].getFil()):
                app.Application.mis_focos[self.num].cambiacolor()

        #Verificar cuantos focos quedan encendidos
        app.Application.totalOn(app.Application)

    def cambiacolor(self):
        if self.cget('bg') == 'grey':
            self.configure(bg='green')
            self.on = True
        else:
            self.configure(bg='grey')
            self.on = False
        #Solo para debuggear
        print(self.num)
        print(self.on)

    def getOn(self):
        return self.on

    def getFil(self):
        return self.fil

    def setFil(self, n):
        self.fil = n

    def getCol(self):
        return self.col

    def setCol(self, n):
        self.col = n




