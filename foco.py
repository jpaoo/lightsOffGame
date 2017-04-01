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

        #Se va a calcular el numeo de columnas para poder encender/apagar los focos de forma vertical
        lenCols = len(app.Application.mis_focos)
        #numCols es la cantidad de columnas totales que tiene el juego, por lo que es lo que se va a incrementar/decrementar para encender/apagar de forma vertical
        numCols = app.Application.mis_focos[self.num-self.num+lenCols-1].getCol()
        numFils = app.Application.mis_focos[self.num - self.num + lenCols - 1].getFil()


        #Encender/Apagar el foco de arriba, verificando que si existe primero
        if(app.Application.mis_focos[self.num - numCols-2].getFil() != numFils and app.Application.mis_focos[self.num-1] != numCols):
            if(app.Application.mis_focos[self.num - numCols-2].getCol() <= numCols and app.Application.mis_focos[self.num-1].getFil() >= 0):
                app.Application.mis_focos[self.num - numCols-2].cambiacolor()

        #Encender/Apagar el foco de abajo, verificando este exista
        if(app.Application.mis_focos[self.num-1].getFil() <= numFils - 1):
            if (app.Application.mis_focos[self.num + numCols].getCol() <= numCols):
                app.Application.mis_focos[self.num + numCols].cambiacolor()
        #Verificar cuantos focos quedan encendidos
        app.Application.totalOn(app.Application)
        app.Application.setIntentos(app.Application, 1)
        app.Application.finJuego(app.Application)
        print("Intentos: ", app.Application.getIntentos(app.Application))

    def cambiacolor(self):
        if self.cget('bg') == 'grey':
            self.configure(bg='green')
            self.on = True
        else:
            self.configure(bg='grey')
            self.on = False

    def setOn(self, n):
        self.on = n

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




