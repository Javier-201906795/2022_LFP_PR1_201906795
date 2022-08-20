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
                mensaje += "Error en la linea No. " + str(i+1) + " Faltan Campos; Campos encontrados: "+ str(NoCampos) + "\n"
            elif (NoCampos > 7):
                mensaje += "Error en la linea No. " + str(i+1) + " exiten Campos EXTRA;  Campos encontrados: "+ str(NoCampos) + "\n"
            
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
def validadorcodigocurso(_listaElementos,ini,titulo):
    try:
        mensajeerror = ""
        #█═══════════════[ Validar es Codigo ] ══════════════════════════════════█
        #Valida si es un numero positivo menor a o igual a 3
        for i in range(0,len(_listaElementos)):
            #──O────────────────O─
            validadornum = Bvalidadornumero(_listaElementos[i][ini])
            #Validador si es un numero
            if(validadornum == True):
                #──O────────────────O─
                #Validar si es un numero Positivo
                if(int(_listaElementos[i][ini]) > 0 ):
                    #──O────────────────O─
                    #Quitar ceros a la izquierda
                    numero= int(_listaElementos[i][ini])
                    #──O────────────────O─
                    #Validar si es un numero de 3 digitos
                    if(numero <= 999):
                        None
                    else:
                        #──O────────────────O─
                        #No es un codigo valido
                        mensajeerror += "Linea " + str(i+1) + " (Error: No es un codigo Valido), "    
                else:
                    #──O────────────────O─
                    #No es un positivo
                    mensajeerror += "Linea " + str(i+1) + " (Error: No es un numero Positivo), "    
            else:
                #──O────────────────O─
                #No es un numero 
                mensajeerror += "Linea " + str(i+1) + " (Error: No es un numero), "
        #──O────────────────O─
        if (mensajeerror == ""):
            #──O────────────────O─
            #No hay errores de Codigo
            return True
        else:
            #──O────────────────O─
            VNT0.Mostrar("Error [Segmentador SEG2]: Revisar campo "+titulo+" en las siguiente lineas: " + mensajeerror)
            return False
                
        
        #──O────────────────O─
    except Exception as e:
        VNT0.Mostrar("Error [Segmentador SEG2]: Ocurrio un erro al validar codigo curso. \n"+str(e))
        return None

#————————————————————»✦«—————————————————————————————————————————————————##
#Boolean #Reusable
def Bvalidadornumero(textonum):
    try:
        numero = int(textonum)
        return True
    except Exception as e:
        return False
    

#————————————————————»✦«—————————————————————————————————————————————————#
def exportarValidadores(listaElementos):
    # print("Lista: ", listaElementos)
    #█═══════════════[ Validar si no hay campos extra o faltantes ] ══════════════════════════════════█
    #funcion devuleve True o False
    Validadorcamposextras = validadorcamposextra(listaElementos)
    
    #Validador Boolean si el Codigo del curso esta bien
    if (Validadorcamposextras == False):
        #█═══════════════[ Validar Codigo Curso ] ══════════════════════════════════█
        #──O────────────────O─
        Validadorcodigocurso = validadorcodigocurso(listaElementos,0,"codigo carrera")
        print("Validando Codigo curso.... ",Validadorcodigocurso)
        #█═══════════════[ Validar Prerequisitos Curso ] ══════════════════════════════════█

        #──O────────────────O─
        
    

    