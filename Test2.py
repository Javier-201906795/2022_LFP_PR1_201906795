import tkinter as tk

import Test3 as f






def dest(_ven):
    _ven.destroy()




if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.geometry('500x500')
    ventana.title('Ejemplo clase 4')

    tk.Label(ventana, text='Nombre1: ').place(x=50, y=50)
    tk.Label(ventana, text='Apellido1: ').place(x=50, y=75)
    tk.Label(ventana, text='Edad1: ').place(x=50, y=100)
    tk.Label(ventana, text='Genero1: ').place(x=50, y=125)

    nombre = tk.StringVar()
    apellido = tk.StringVar()
    edad = tk.StringVar()
    genero = tk.StringVar()
    tk.Entry(ventana, textvariable=nombre).place(x=150, y=50)
    tk.Entry(ventana, textvariable=apellido).place(x=150, y=75)
    tk.Entry(ventana, textvariable=edad).place(x=150, y=100)
    tk.Entry(ventana, textvariable=genero).place(x=150, y=125)

    tk.Button(ventana, text='Enviar', command= lambda : f.enviarInformacion(ventana, nombre, apellido, edad, genero)).place(x=300, y=125)

    ventana.mainloop()


# pip 

# pip install pyinstaller

# pyinstaller  tu_script.py