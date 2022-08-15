#╔══════════════════════════════════╗
#║ PROYECTO 1 LFP                   ║
#║ JAVIER  RICARDO YLLESCAS BARRIOS ║
#║ CARNE: 201906795                 ║
#╚══════════════════════════════════╝

#──O────────────────O──
#————————————————————»✦«—————————————————————————————————————————————————#
#█┼┼┼┼┼┼┼┼┼┼┼|  |┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#█═══════════════[  ] ══════════════════════════════════█

#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT1_Inicio as VNT1






#————————————————————»✦«—————————————————————————————————————————————————#

#————————————————————»✦«—————————————————————————————————————————————————#
def Mensajeinicio():

    print("╔══════════════════════════════════╗")
    print("║ PROYECTO 1 LFP                   ║")
    print("║ JAVIER  RICARDO YLLESCAS BARRIOS ║")
    print("║ CARNE: 201906795                 ║")
    print("╚══════════════════════════════════╝")





#█┼┼┼┼┼┼┼┼┼┼┼| MAIN |┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
if __name__ == '__main__':

    #█═══════════════[ Mensaje Inicio ] ══════════════════════════════════█
    
    Mensajeinicio()

    #█═══════════════[ Ventana Principal ] ══════════════════════════════════█
    #──O────────────────O─────────────────
    #Iniciar Ventana principal con tkinter
    VentanaPrincipal = tk.Tk()
    #──O────────────────O────────────────────────────────
    #Funcion con interfaz grafica de la Ventana Principal
    VNT1.Mostrar(VentanaPrincipal)
    #──O────────────────O─────────────────────
    #Mantiene la Ventana Principal funcionando
    VentanaPrincipal.mainloop()
