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
    
#————————————————————»✦«—————————————————————————————————————————————————#
def Mostrar():
    #──O────────────────O────────────────────
    #Variable para verficar si esta abierta la ventana
    global VNTAbierta
    if (VNTAbierta == False):
        #█═══════════════[ Ventana ] ═════════════════════════════════█
        global ventana
        ventana = tk.Toplevel()
        ventana.geometry('450x550')
        ventana.title('Contero de Creditos')
        #──O────────────────O───
        #Observador Boton Cerrar
        ventana.protocol("WM_DELETE_WINDOW",Cerrar)
        #█═══════════════[ Texto ] ═════════════════════════════════█
        #──O────────────────O───
        #Variables
        global creditosaprobados, creditoscursando, creditospendientes, creditosobligatorios, creditossemestre
        creditosaprobados = -1
        creditoscursando = -2
        creditospendientes = -3
        
        creditosobligatorios = -1
        creditossemestre = -1


        tk.Label(ventana, text='Creditos Aprobados: ' + str(creditosaprobados)).place(x=20, y=20)
        tk.Label(ventana, text='Creditos Cursando: ' + str(creditoscursando)).place(x=20, y=70)
        tk.Label(ventana, text='Creditos Pendientes: ' + str(creditospendientes)).place(x=20, y=140)
        tk.Label(ventana, text='Creditos Obligatorios hasta el semestre N: ').place(x=20, y=210)
        tk.Label(ventana, text='Semestre: ').place(x=20, y=280)
        tk.Label(ventana, text='Creditos del Semestre: ').place(x=20, y=340)
        tk.Label(ventana, text='Semestre: ').place(x=20, y=410)
        #█═══════════════[ Input ] ═════════════════════════════════█
        global vsemestre1, vsemestre2, nosemestre1, nosemestre2
        vsemestre1 = tk.StringVar()
        vsemestre2 = tk.StringVar()
        nosemestre1 = tk.StringVar()
        nosemestre2 = tk.StringVar()
        #──O────────────────O───
        tk.Entry(ventana, textvariable=vsemestre1).place(x=250, y=210)
        tk.Entry(ventana, textvariable=nosemestre1).place(x=80, y=280)
        tk.Entry(ventana, textvariable=vsemestre2).place(x=150, y=340)
        tk.Entry(ventana, textvariable=nosemestre2).place(x=80, y=410)
        #█═══════════════[ Boton ] ═════════════════════════════════█
        tk.Button(ventana, text='Contar', command= lambda : conteocreditosobligatorios()).place(x=210, y=275)
        tk.Button(ventana, text='Contar', command= lambda : conteocreditossemestre()).place(x=210, y=405)
        tk.Button(ventana, text='Regresar', command= lambda : Cerrar()).place(x=360, y=480)
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
def validadoresinputs(semestre1, semestre2, tipo):
    try:
        #──O────────────────O───────
        #Validador
        semestreinicio = int(semestre1)
        semestrefin = int(semestre2)
        return True

    except Exception as e:
        mensajeerror = "Porfavor ingrese valores numericos en " + tipo
        VNT0.Mostrar(mensajeerror)
        #──O────────────────O───────
        #Validador
        return False
        
#————————————————————»✦«—————————————————————————————————————————————————#
def conteocreditosobligatorios():
    #█═══════════════[ Obtner inputs ] ═════════════════════════════════█
    semestreinicio = vsemestre1.get()
    semestrefin = nosemestre1.get()
    #█═══════════════[ Validar inputs ] ═════════════════════════════════█
    #──O────────────────O───────
    valornumerico = validadoresinputs(semestreinicio,semestrefin, "CREDITOS OBLIGATORIOS")
#    print("valor numerico es:  ", valornumerico)
    #█═══════════════[ Conteo creditos obligatorios ] ═════════════════════════════════█
    if (valornumerico == True):
        print("contando creditos obligatorios")



#————————————————————»✦«—————————————————————————————————————————————————#
def conteocreditossemestre():
    #█═══════════════[ Obtner inputs ] ═════════════════════════════════█
    semestreinicio = vsemestre2.get()
    semestrefin = nosemestre2.get()
    #█═══════════════[ Validar inputs ] ═════════════════════════════════█
    #──O────────────────O───────
    valornumerico = validadoresinputs(semestreinicio,semestrefin, "CREDITOS DEL SEMESTRE")
#    print("valor numerico es:  ", valornumerico)
    #█═══════════════[ Conteo creditos semestre ] ═════════════════════════════════█
    if (valornumerico == True):
        print("contando creditos semestre")
