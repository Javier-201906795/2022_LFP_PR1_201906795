#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS

def test():
    print("hola")

def Mostrar():
    _nombre = "test1"
    _apellido = "test2"
    _edad = "test3"
    _genero = "test4"
    ventana = tk.Toplevel()
    ventana.geometry('500x500')
    tk.Label(ventana, text='INFORMACION DEL USUARIO1').place(x=50, y=275)
    tk.Label(ventana, text='Mi nombre es').place(x=50, y=300)
    tk.Label(ventana, textvariable=_nombre).place(x=150, y=300)
    tk.Label(ventana, text='Mi Apellido es').place(x=50, y=325)
    tk.Label(ventana, textvariable=_apellido).place(x=150, y=325)
    tk.Label(ventana, text='Mi edad es').place(x=50, y=350)
    tk.Label(ventana, textvariable=_edad).place(x=150, y=350)
    tk.Label(ventana, text='Mi genero es').place(x=50, y=375)
    tk.Label(ventana, textvariable=_genero).place(x=150, y=375)
    tk.Button(ventana, text='CERRAR', command= lambda : T.dest(_ventana)).place(x=50, y=50)
    ventana.mainloop()

def Cerrar(ventana):
    ventana.destroy()

