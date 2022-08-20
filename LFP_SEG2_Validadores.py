#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import LFP_VNT0_Errores as VNT0


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#————————————————————»✦«—————————————————————————————————————————————————#
def validadorcamposextra(_listaElementos):
    try:
        #──O────────────────O─
        #Valida que no existan valores extra o faltantes
        #Código, Nombre, Prerrequisitos, Obligatorio, Semestre, Créditos, Estado
        #  0   ,   1   ,       2       ,      3     ,    4    ,    5    ,   6 
        mensaje = ""
        #──O────────────────O─
        for i in range (0,len(_listaElementos)):
            #──O────────────────O─
            #obtiene el numero de campos por elemento
            NoCampos = len(_listaElementos[i])
            #──O────────────────O─
            #Valida si no faltan campos
            if (NoCampos < 7):
                mensaje += "Error en la linea No. " + str(i) + " Faltan Campos; Campos encontrados: "+ str(NoCampos) + "\n"
            elif (NoCampos > 7):
                mensaje += "Error en la linea No. " + str(i) + " exiten Campos EXTRA;  Campos encontrados: "+ str(NoCampos) + "\n"
            
        #──O────────────────O─
        # Validador
        if (mensaje != ""):
            VNT0.Mostrar("Error [Segmentador SEG2]: Deben de ser 7 Campos  \n"+ mensaje)
            return True
        else:
            return False
        #──O────────────────O─
    except Exception as e:
        VNT0.Mostrar("Error [Segmentador SEG2]: Ocurrio un error al validar campos extra o faltantes \n " + str(e))


#————————————————————»✦«—————————————————————————————————————————————————#
def exportarValidadores(listaElementos):
    # print("Lista: ", listaElementos)
    #█═══════════════[ Validar si no hay campos extra o faltantes ] ══════════════════════════════════█
    #funcion devuleve True o False
    Validadorcamposextras = validadorcamposextra(listaElementos)
    #█═══════════════[ Validar Codigo Curso ] ══════════════════════════════════█
    #──O────────────────O─
    #Validador 
    if (Validadorcamposextras == False):
        print("Validando Codigo curso....")
    

    