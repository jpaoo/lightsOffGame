from app import *

x = 0
while x < 5:
    x = int(input('Cuantas columnas quiere: '))
    if x < 5:
        print("El minimo de columnas es de 5")
y = 0
while y < 5:
    y = int(input('Cuantas filas quiere: '))
    if y < 5:
        print("El minimo tamaño para las filas es de 5")

dif = 0
while dif > 3 or dif < 1:
    dif = int(input('Nivel de dificultad 1) Facil 2) Medio 3) Dificil: '))
    if dif > 3 or dif < 1:
        print("Elija una dificultad adecuada")

intentos = 0

root = Tk()
root.title("Apaga las luces")

#Configurar el grid para que los botones se ajusten y poder acomodarlos por columnas
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Ya no se utiliza, se usa solo para poner el grid de tamaño fijo
#root.geometry("500x300")

app = Application(root, x, y, dif, intentos)
root.mainloop()