#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
from tkinter import filedialog
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT0_Errores as VNT0
import LFP_VNT2_0_Gestionar_Cursos as VNT2
import LFP_VNT3_0_Conteo_Creditos as VTN3
import LFP_SEG1_Segmentador_datos as SEG1


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
global Texto
Texto = " "

#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█

#————————————————————»✦«—————————————————————————————————————————————————#

def test():
    print("hola")

#————————————————————»✦«—————————————————————————————————————————————————#
def Mostrar(ventana):
    #█═══════════════[ Ventana ] ═════════════════════════════════█
    ventana.geometry('600x500')
    ventana.title('PRACTICA 1')
    #█═══════════════[ Textos ] ══════════════════════════════════█
    tk.Label(ventana, text='Lab. Lenguajes Formales y de Programacion').place(x=50, y=10)
    tk.Label(ventana, text='Nombre del estudiante: Javier Ricardo Yllescas Barrios').place(x=50, y=30)
    tk.Label(ventana, text='Carne del estudiante: 201906795').place(x=50, y=50)
    #█═══════════════[ Botones ] ══════════════════════════════════█
    tk.Button(ventana, text='Cargar Archivo', command= lambda : SeleccionarArchivo()).place(x=250, y=150)
    tk.Button(ventana, text='Gestionar Cursos', command= lambda : VNT2.Mostrar()).place(x=250, y=190)
    tk.Button(ventana, text='Conteo de Creditos', command= lambda : VTN3.Mostrar()).place(x=250, y=230)
    tk.Button(ventana, text='Salir', command= lambda : Cerrar(ventana)).place(x=250, y=270)

#————————————————————»✦«—————————————————————————————————————————————————#
def Cerrar(ventana):
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
        #──O────────────────O──────────
        #guardar en una variable global
        global Texto
        Texto = text
        #──O────────────────O──────────
        #Imprime valores
        print("\n================================")
        print(text)
        print("\n================================")
        #──O────────────────O──────────
        #Validar si esta vacio el archivo
        if (Texto == "" or Texto == " " or Texto == "   "):
            VNT0.Mostrar("El archivo seleccionado esta vacio.")    
        else:
            VNT0.Mostrar("El archivo fue leido con exito.")
            #──O────────────────O──────────
            #Funciones para segmentar los datos,
            SEG1.exportartexto(text)
            

        
    except Exception as e:
        VNT0.Mostrar("Error al seleccionar el archivo. /n " + str(e))

