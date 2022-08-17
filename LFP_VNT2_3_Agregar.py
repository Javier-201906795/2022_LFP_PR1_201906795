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
def Mostrar():
    #──O────────────────O────────────────────
    #Declar variable global para poder usarla
    global VNTAbierta
    if (VNTAbierta == False):
        #█═══════════════[ Ventana ] ═════════════════════════════════█
        global ventana
        ventana = tk.Toplevel()
        ventana.geometry('380x340')
        ventana.title('Agregar')
        #──O────────────────O───
        #Observador Boton Cerrar
        ventana.protocol("WM_DELETE_WINDOW",Cerrar)
        #█═══════════════[ Texto ] ═════════════════════════════════█
        tk.Label(ventana, text='Codigo: ').place(x=50, y=50)
        tk.Label(ventana, text='Nombre: ').place(x=50, y=75)
        tk.Label(ventana, text='Pre Requisito: ').place(x=50, y=100)
        tk.Label(ventana, text='Semestre: ').place(x=50, y=125)
        tk.Label(ventana, text='Opcionalidad: ').place(x=50, y=150)
        tk.Label(ventana, text='Creditos: ').place(x=50, y=175)
        tk.Label(ventana, text='Estados: ').place(x=50, y=200)
        #█═══════════════[ Input ] ═════════════════════════════════█
        global vcodigo, vnombre, vprerequisito, vsemestre,vopcionalidad, vcreditos, vestados
        vcodigo = tk.StringVar()
        vnombre = tk.StringVar()
        vprerequisito = tk.StringVar()
        vsemestre = tk.StringVar()
        vopcionalidad = tk.StringVar()
        vcreditos = tk.StringVar()
        vestados = tk.StringVar()
        tk.Entry(ventana, textvariable=vcodigo).place(x=150, y=50)
        tk.Entry(ventana, textvariable=vnombre).place(x=150, y=75)
        tk.Entry(ventana, textvariable=vprerequisito).place(x=150, y=100)
        tk.Entry(ventana, textvariable=vsemestre).place(x=150, y=125)
        tk.Entry(ventana, textvariable=vopcionalidad).place(x=150, y=150)
        tk.Entry(ventana, textvariable=vcreditos).place(x=150, y=175)
        tk.Entry(ventana, textvariable=vestados).place(x=150, y=200)
        #█═══════════════[ Boton ] ═════════════════════════════════█
        tk.Button(ventana, text='Agregar', command= lambda : Agregar()).place(x=150, y=250)
        tk.Button(ventana, text='Regresar', command= lambda : Cerrar()).place(x=250, y=250)
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
def Agregar():
    #█═══════════════[ Variables (Convertidas a Texto) ] ═════════════════════════════════█
    global tcodigo, tnombre, tprerequisito, tsemestre, topcionalidad, tcreditos, testados
    tcodigo = vcodigo.get()
    tnombre = vnombre.get()
    tprerequisito = vprerequisito.get()
    tsemestre = vsemestre.get()
    topcionalidad = vopcionalidad.get()
    tcreditos = vcreditos.get()
    testados = vestados.get()
    #──O────────────────O───────
    #Tabla para evaluar datos
    ListaInputs = [tcodigo, tnombre,tprerequisito,tsemestre, topcionalidad, tcreditos, testados]
    ListaInputsNombres = ["Codigo", "Nombre", "Pre requisito","Semestre","Opcionalidad", "Creditos", "Estados"]
    #──O────────────────O───────
    #Imprimir Tablas
    #print(ListaInputsNombres)
    #print(ListaInputs)
    #█═══════════════[ Evaluar Espacios Vacios ] ═════════════════════════════════█
    #──O────────────────O───────
    #Ciclo for para evaluar
    finfor = len(ListaInputs)
    #──O────────────────O───────
    #espacios vacios
    global espaciosVacios, mensaje
    espaciosVacios = False
    validador = -1
    mensaje = ""
    for i in range(0,finfor):
        if(ListaInputs[i] == "" or ListaInputs[i] == " " or ListaInputs[i] == "  "):
            validador += 1
            if validador == 0:
                mensaje = "Porfavor llenar todos los espacios. Espacio vacio en "
            mensaje += " " + str(ListaInputsNombres[i]) + ", "
            espaciosVacios = True
            
    #──O────────────────O───────
    #Imprimir mensaje
    
    print("--------------------------------------")
    if (len(mensaje) > 0):
        print("mensaje: ",mensaje)
        VNT0.Mostrar(mensaje)
    print(espaciosVacios)
    print("--------------------------------------")

    #█═══════════════[ Evaluar Inputs ] ═════════════════════════════════█

    #█═══════════════[ Imprimir Inputs ] ═════════════════════════════════█
    
    
    
