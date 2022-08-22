#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#──O────────────────O────────
#LIBRERIAS VENTANA GRAFICA
import tkinter as tk
from tkinter import filedialog
#──O────────────────O────────
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT0_Errores as VNT0
import LFP_CRUD_DB as CRUD
import LFP_CRUD_DB2 as CRUD2

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
def Mostrar(_codigo):
    _codigo -= 1 
    print("CODIGO A EDITAR: ",_codigo)
    #──O────────────────O────────────────────
    #Declar variable global para poder usarla
    global VNTAbierta
    if (VNTAbierta == False):
        #█═══════════════[ Ventana ] ═════════════════════════════════█
        global ventana
        ventana = tk.Toplevel()
        ventana.geometry('380x340')
        ventana.title('Editar etes')
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
        #──O────────────────O───
        #Obtiene Listado 
        ListadoDB = CRUD.leerdb()

        #Colocar valores (Texto)
        vcodigo.set(str(ListadoDB[_codigo][0]))
        vnombre.set(str(ListadoDB[_codigo][1]))
        vprerequisito.set(str(ListadoDB[_codigo][2]))
        vsemestre.set(str(ListadoDB[_codigo][3]))
        vopcionalidad.set(str(ListadoDB[_codigo][4]))
        vcreditos.set(str(ListadoDB[_codigo][5]))
        vestados.set(str(ListadoDB[_codigo][6]))
        #──O────────────────O───
        global entrycodigo
        entrycodigo = tk.Entry(ventana, textvariable=vcodigo).place(x=150, y=50)
        tk.Entry(ventana, textvariable=vnombre).place(x=150, y=75)
        tk.Entry(ventana, textvariable=vprerequisito).place(x=150, y=100)
        tk.Entry(ventana, textvariable=vsemestre).place(x=150, y=125)
        tk.Entry(ventana, textvariable=vopcionalidad).place(x=150, y=150)
        tk.Entry(ventana, textvariable=vcreditos).place(x=150, y=175)
        tk.Entry(ventana, textvariable=vestados).place(x=150, y=200)
        #█═══════════════[ Boton ] ═════════════════════════════════█
        tk.Button(ventana, text='Editar', command= lambda : Editar()).place(x=150, y=250)
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
def Editar():
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
    else: 
        #──O────────────────O───────
        #Imprimir Tablas
        print(ListaInputsNombres)
        print(ListaInputs)
    # print(espaciosVacios)
    

    #█═══════════════[ Evaluar Inputs ] ═════════════════════════════════█
        #Evaluar si es un numero
        sonnumeros = True
        try:
            mensaje = ""
            for i in range(0,len(ListaInputs)):
                if ( i == 1 or i==2):
                    None
                else:
                    try:
                        numero = int(ListaInputs[i])
                    except Exception as e:
                        mensaje += str(ListaInputsNombres[i]) + ", "
            
            if (mensaje != ""):
                mensaje = "Error por favor agrege un valor numerico en: " + mensaje
                VNT0.Mostrar(mensaje)
                sonnumeros = False
        except Exception as e:
            VNT0.Mostrar("error " + e)
        #█═══════════════[ Listar Inputs ] ═════════════════════════════════█
        ListaCurso = [tcodigo, tnombre,tprerequisito,tsemestre,topcionalidad,tcreditos,testados]
        #█═══════════════[ CRUD GUARDAR ] ═════════════════════════════════█
        if (sonnumeros == True):
            CRUD2.agregarcurso(ListaCurso)
            VNT0.Mostrar("Se edito el curso correctamento de LFP_DB.csv")
            Cerrar()
    
    
