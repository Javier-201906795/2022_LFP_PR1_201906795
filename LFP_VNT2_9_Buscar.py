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

#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█

#————————————————————»✦«—————————————————————————————————————————————————#
def test():
    print("test")
    print(vcodigo.get())
    if(vcodigo.get() == " " or vcodigo.get() == ""):
        print("vacio")
#————————————————————»✦«—————————————————————————————————————————————————#
def Mostrar(_Accion):
    #──O────────────────O────────────────────
    #Varibles para editar o eliminar
    global Accion 
    Accion = _Accion
    #──O────────────────O────────────────────
    #Declar variable global para poder usarla
    global VNTAbierta
    if (VNTAbierta == False):
        #█═══════════════[ Ventana ] ═════════════════════════════════█
        global ventana
        ventana = tk.Toplevel()
        ventana.geometry('300x120')
        ventana.title(_Accion)
        #──O────────────────O───
        #Observador Boton Cerrar
        ventana.protocol("WM_DELETE_WINDOW",Cerrar)
        #█═══════════════[ Texto ] ═════════════════════════════════█
        tk.Label(ventana, text='No. Curso: ').place(x=10, y=10)
        #█═══════════════[ Input ] ═════════════════════════════════█
        global vcodigo
        vcodigo = tk.StringVar()
        #──O────────────────O───
        tk.Entry(ventana, textvariable=vcodigo).place(x=110, y=10)
        #█═══════════════[ Boton ] ═════════════════════════════════█
        tk.Button(ventana, text='Buscar', command= lambda : Buscar()).place(x=120, y=60)
        tk.Button(ventana, text='Regresar', command= lambda : Cerrar()).place(x=200, y=60)
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
def Buscar():
    #█═══════════════[ Variables (Convertidas a Texto) ] ═════════════════════════════════█
    global tcodigo
    tcodigo = vcodigo.get()
    #──O────────────────O───────
    #Tabla para evaluar datos
    ListaInputs = [tcodigo]
    ListaInputsNombres = ["Codigo"]
    
    #█═══════════════[ Evaluar Espacios Vacios ] ═════════════════════════════════█
    #──O────────────────O───────
    #Ciclo for para evaluarpy
    finfor = len(ListaInputs)
    #──O────────────────O───────
    #espacios vacios
    global espaciosVacios, mensaje
    espaciosVacios = False
    validador = -1
    mensaje = ""
    for i in range(0,finfor):
        #Evalua
        if(ListaInputs[i] == "" or ListaInputs[i] == " " or ListaInputs[i] == "  "):
            #si hay espacio vacios
            validador += 1
            #Mensaje activacion 
            if validador == 0:
                mensaje = "Porfavor llenar todos los espacios. Espacio vacio en "
            #valores vacios
            mensaje += " " + str(ListaInputsNombres[i]) + " "
            #validador
            espaciosVacios = True
            
    #──O────────────────O───────
    #Imprimir mensaje
    if (len(mensaje) > 0):
        # print("mensaje: ",mensaje)
        VNT0.Mostrar(mensaje)
    
    #──O────────────────O───────
    #Imprimir Tablas
    # print(ListaInputsNombres)
    # print(ListaInputs)
    # print(espaciosVacios)
    #█═══════════════[ Evaluar Inputs ] ═════════════════════════════════█
    #──O────────────────O───────
    global codigocurso
    codigocurso = -1
    #Evalua si es un numero 
    try:
        #──O────────────────O───────
        #Evaluar si no esta vacio
        if (espaciosVacios == False):
            #──O────────────────O───────
            #Evaluar dato si se puede convertir a texto
            
            codigocurso = int(tcodigo)
        
    except Exception as e:
        #──O────────────────O───────
        #Si no se puede convertir a numero
        mensajeerror = "Error: Porfavor ingrese un valor numerico"
        VNT0.Mostrar(mensajeerror)
    
    #──O────────────────O─────── 
    #Evalua si es un numero no mayor a 3 digitos
    codigocorrecto = True
    if (codigocurso > 999 or codigocurso < 0):
        if(codigocurso != -1):
            codigocorrecto = False
            mensajeerror = "Error: Porfavor ingrese un codigo valido. (3 digitos) (Positivo)"
            VNT0.Mostrar(mensajeerror)

    #█═══════════════[ Ejecutar Accion ] ═════════════════════════════════█
    #print("Accion", Accion)
    if (espaciosVacios == False and codigocorrecto == True):
        if (Accion == "EDITAR"):
            AccEditar(codigocurso)
        elif (Accion == "ELIMINAR"):
            AccEliminar(codigocurso)
        else:
            mensaje("Porblemas al buscar coloque una accion valida")
            VNT0.Mostrar(mensaje)

#————————————————————»✦«—————————————————————————————————————————————————#
def AccEditar(codigo):
    print("Editando ", codigo)

#————————————————————»✦«—————————————————————————————————————————————————#
def AccEliminar(codigo):
    print("Eliminando ", codigo)



    
    
    
