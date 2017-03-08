from tkinter import *


class Foco(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs, command=self.cambiacolor)
        self['bg'] = 'grey'

    def cambiacolor(self):
        if self.cget('bg') == 'grey':
            self.configure(bg='green')
        else:
            self.configure(bg='grey')


