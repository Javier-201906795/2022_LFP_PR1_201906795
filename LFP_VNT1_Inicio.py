#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT2_Seleccionar_archivo as VNT2

#————————————————————»✦«—————————————————————————————————————————————————#

def test():
    print("hola")

#————————————————————»✦«—————————————————————————————————————————————————#
def Mostrar(ventana):
    ventana.geometry('600x500')
    ventana.title('PRACTICA 1')
    #█═══════════════[ Textos ] ══════════════════════════════════█
    tk.Label(ventana, text='Lab. Lenguajes Formales y de Programacion').place(x=50, y=10)
    tk.Label(ventana, text='Nombre del estudiante: Javier Ricardo Yllescas Barrios').place(x=50, y=30)
    tk.Label(ventana, text='Carne del estudiante: 201906795').place(x=50, y=50)
    #█═══════════════[ Botones ] ══════════════════════════════════█
    tk.Button(ventana, text='Cargar Archivo', command= lambda : VNT2.Mostrar()).place(x=250, y=150)
    tk.Button(ventana, text='Gestionar Cursos', command= lambda : test()).place(x=250, y=190)
    tk.Button(ventana, text='Conteo de Creditos', command= lambda : test()).place(x=250, y=230)
    tk.Button(ventana, text='Salir', command= lambda : Cerrar(ventana)).place(x=250, y=270)

#————————————————————»✦«—————————————————————————————————————————————————#
def Cerrar(ventana):
    ventana.destroy()

