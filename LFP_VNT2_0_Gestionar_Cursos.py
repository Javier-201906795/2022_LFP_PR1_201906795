#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
from tkinter import filedialog
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT0_Errores as VNT0
import LFP_VNT2_2_Editar as VNT2_2
import LFP_VNT2_3_Agregar as VNT2_3
import LFP_VNT2_9_Buscar as VNT9

#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBALES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O───────────
#Validador de ventanas repetidas
global VNTAbierta
VNTAbierta = False

#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█

#————————————————————»✦«—————————————————————————————————————————————————#
def test():
    print("test")
#————————————————————»✦«—————————————————————————————————————————————————#
def Mostrar():
    #──O────────────────O────────────────────
    #Declar variable global para poder usarla
    global VNTAbierta
    if (VNTAbierta == False):
        #█═══════════════[ Ventana ] ═════════════════════════════════█
        global ventana
        ventana = tk.Toplevel()
        ventana.geometry('300x250')
        #──O────────────────O───
        #Observador Boton Cerrar
        ventana.protocol("WM_DELETE_WINDOW",Cerrar)
        #█═══════════════[ Boton ] ═════════════════════════════════█
        tk.Button(ventana, text='Listar Cursos', command= lambda : test()).place(x=100, y=30)
        tk.Button(ventana, text='Agregar Curso', command= lambda : VNT2_3.Mostrar()).place(x=100, y=70)
        tk.Button(ventana, text='Editar Curso', command= lambda : VNT9.Mostrar("EDITAR")).place(x=100, y=110)
        tk.Button(ventana, text='Eliminar Curso', command= lambda : VNT9.Mostrar("ELIMINAR")).place(x=100, y=150)
        tk.Button(ventana, text='Regresar', command= lambda : Cerrar()).place(x=100, y=190)
        #█═══════════════[ Validador ] ═════════════════════════════════█
        VNTAbierta = True
        #──O────────────────O───────
        #Mantiene la ventana abierta
        ventana.mainloop()
    else:
        VNT0.Mostrar("La ventana ya esta abierta.")

    
#————————————————————»✦«—————————————————————————————————————————————————#
def Cerrar():
    global VNTAbierta
    VNTAbierta = False
    ventana.destroy()
