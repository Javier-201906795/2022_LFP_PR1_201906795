#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
from tkinter import filedialog
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT0_Errores as VNT0
import LFP_VNT2_3_Agregar as VNT2_3
import LFP_VNT2_9_Buscar as VNT9
import LFP_CRUD_DB as CRUD



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
        ventana.geometry('500x500')
        #──O────────────────O───
        #Observador Boton Cerrar
        ventana.protocol("WM_DELETE_WINDOW",Cerrar)
        #█═══════════════[ Texto] ═════════════════════════════════█
        ListadoDB = CRUD.leerdb()
        print(ListadoDB)
        texto = str(ListadoDB)

        _mensaje = texto
        #█═══════════════[ Evaluar mensaje ] ═════════════════════█
        #──O────────────────O────────
        #Evalua si un texto largo y agrega saltos de linea
        if (len(texto) > 90 and len(texto) < 180):
            _mensaje = texto[0:90] + ' -\n'
            _mensaje += texto[90:len(texto)]
        elif (len(texto) > 180 and len(texto) < 270):
            _mensaje = texto[0:90] + ' -\n'
            _mensaje += texto[91:180] + ' -\n'
            _mensaje += texto[181:len(texto)] + '\n'
        elif (len(texto) > 270):
            _mensaje = texto[0:90] + ' -\n'
            _mensaje += texto[91:180] + ' -\n'
            _mensaje += texto[181:270] + ' -\n'
            _mensaje += texto[271:350] + '..... \n'
            



        tk.Label(ventana, text=_mensaje).place(x=50, y=10)
        #█═══════════════[ Boton ] ═════════════════════════════════█
        tk.Button(ventana, text='Regresar', command= lambda : Cerrar()).place(x=150, y=450)
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
