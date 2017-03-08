from app import *

root = Tk()
root.title("Apaga las luces")


#Configurar el grid para que los botones se ajusten y poder acomodarlos por columnas
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Ya no se utiliza, se usa solo para poner el grid de tamaño fijo
#root.geometry("500x300")

app = Application(root)

root.mainloop()
