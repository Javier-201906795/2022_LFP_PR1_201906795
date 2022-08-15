import tkinter as tk
import Test2 as T

def enviarInformacion(_ventana, _nombre, _apellido, _edad, _genero):
    _ventana = tk.Toplevel()
    _ventana.geometry('500x500')
    tk.Label(_ventana, text='INFORMACION DEL USUARIO1').place(x=50, y=275)
    tk.Label(_ventana, text='Mi nombre es').place(x=50, y=300)
    tk.Label(_ventana, textvariable=_nombre).place(x=150, y=300)
    tk.Label(_ventana, text='Mi Apellido es').place(x=50, y=325)
    tk.Label(_ventana, textvariable=_apellido).place(x=150, y=325)
    tk.Label(_ventana, text='Mi edad es').place(x=50, y=350)
    tk.Label(_ventana, textvariable=_edad).place(x=150, y=350)
    tk.Label(_ventana, text='Mi genero es').place(x=50, y=375)
    tk.Label(_ventana, textvariable=_genero).place(x=150, y=375)
    tk.Button(_ventana, text='CERRAR', command= lambda : T.dest(_ventana)).place(x=50, y=50)
    _ventana.mainloop()