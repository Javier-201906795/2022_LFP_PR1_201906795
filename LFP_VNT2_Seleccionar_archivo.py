#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
from tkinter import filedialog
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT0_Errores as VNT0

#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBALES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O───────────
#Validador de ventanas repetidas
global VNTAbierta
VNTAbierta = False


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
        ventana.geometry('500x150')
        #──O────────────────O───
        #Observador Boton Cerrar
        ventana.protocol("WM_DELETE_WINDOW",Cerrar)
        #█═══════════════[ Texto ] ═════════════════════════════════█
        tk.Label(ventana, text='Ruta').place(x=50, y=50)
        ruta = tk.StringVar()
        tk.Entry(ventana, textvariable=ruta).place(x=90, y=50)
        #█═══════════════[ Boton ] ═════════════════════════════════█
        tk.Button(ventana, text='Subir Archivo', command= lambda : SeleccionarArchivo()).place(x=150, y=100)
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
#————————————————————»✦«—————————————————————————————————————————————————#
def SeleccionarArchivo():
    try:
        #──O────────────────O─
        #opciones del buscador
        archivo = filedialog.askopenfilename(
        title = "Selecciona un archivo",
        #──O────────────────O─────────────────────
        #accede a la carpeta donde esta el archivo 
        initialdir =  "./",
        #──O────────────────O─────────────────
        #tipo de archivo que puede seleccionar
        filetype = [
            ("Archivos LFP", "*.form"),
            ("Todos los archivos", "*.*")
        ]
        )

        #──O────────────────O─────────────────
        #abre el archivo seleccionado y lo lee
        with open(archivo, 'r', encoding='utf8') as file:
                text = file.read()
                file.close()

        archivo.close()
        #──O────────────────O──────────
        #guardar en una variable global
        global Texto
        Texto = text
        #──O────────────────O──────────
        #imprimir el texto
        
        VNT0.Mostrar("El archivo seleccionado esta vacio.")    
        print(text)
        
        if (Texto == "" or Texto == " "):
            VNT0.Mostrar("El archivo seleccionado esta vacio.")    
        else:
            VNT0.Mostrar("El archivo fue leido con exito.")

        
    except Exception as e:
        VNT0.Mostrar("Error al seleccionar el archivo. /n " + str(e))
