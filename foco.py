from tkinter import *
import app

class Foco(Button):

    def __init__(self, x, *args, **kwargs):
        Button.__init__(self, *args, **kwargs, command=self.botonPressed)
        self['bg'] = 'grey'
        self.num = x
        self.on = False

    def botonPressed(self):
        self.cambiacolor()
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





