#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk


#————————————————————»✦«—————————————————————————————————————————————————#

def test():
    print("hola")

#————————————————————»✦«—————————————————————————————————————————————————#
def Mostrar(mensaje):
    _mensaje = mensaje
    #█═══════════════[ Ventan configuracion ] ═════════════════════█
    ventana = tk.Toplevel()
    ventana.geometry('500x150')
    ventana.title('PRACTICA 1 - MENSAJE')
    #█═══════════════[ Textos ] ═══════════════════════════════════█
    tk.Label(ventana, text= _mensaje).place(x=50, y=10)
    #█═══════════════[ Botones ] ══════════════════════════════════█
    tk.Button(ventana, text='Salir', command= lambda : Cerrar(ventana)).place(x=50, y=100)
    

#————————————————————»✦«—————————————————————————————————————————————————#
def Cerrar(ventana):
    ventana.destroy()

