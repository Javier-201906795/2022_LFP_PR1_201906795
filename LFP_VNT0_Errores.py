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
    #█═══════════════[ Evaluar mensaje ] ═════════════════════█
    #──O────────────────O────────
    #Evalua si un texto largo y agrega saltos de linea
    if (len(mensaje) > 90 and len(mensaje) < 180):
        _mensaje = mensaje[0:90] + ' -\n'
        _mensaje += mensaje[90:len(mensaje)]
        print(_mensaje)
    elif (len(mensaje) > 180 and len(mensaje) < 270):
        _mensaje = mensaje[0:90] + ' -\n'
        _mensaje += mensaje[91:180] + ' -\n'
        _mensaje += mensaje[181:len(mensaje)] + '\n'
    elif (len(mensaje) > 270):
        _mensaje = mensaje[0:90] + ' -\n'
        _mensaje += mensaje[91:180] + ' -\n'
        _mensaje += mensaje[181:270] + ' -\n'
        _mensaje += mensaje[271:350] + '..... \n'
        


    #█═══════════════[ Ventan configuracion ] ═════════════════════█
    ventana = tk.Toplevel()
    ventana.geometry('500x150')
    ventana.title('PRACTICA 1 - MENSAJE')
    #█═══════════════[ Textos ] ═══════════════════════════════════█
    tk.Label(ventana, text= _mensaje).place(x=20, y=10)
    #█═══════════════[ Botones ] ══════════════════════════════════█
    tk.Button(ventana, text='Salir', command= lambda : Cerrar(ventana)).place(x=200, y=110)
    

#————————————————————»✦«—————————————————————————————————————————————————#
def Cerrar(ventana):
    ventana.destroy()

