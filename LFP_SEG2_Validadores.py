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


#————————————————————»✦«—————————————————————————————————————————————————#
def validadorprerequisitos(_listaElementos,ini,titulo):
    try:
        mensajeerror = ""
        #█═══════════════[ Validar es Codigo ] ══════════════════════════════════█
        #Valida si es un numero positivo menor a o igual a 3
        #recorre elementos
        for i in range(0,len(_listaElementos)):
            #recorre campos (prerequisitos)
            for j in range(0,len(_listaElementos[i][ini])):
                #──O────────────────O─
                validadornum = Bvalidadornumero(_listaElementos[i][ini][j])
                #Validador si es un numero
                if(validadornum == True):
                    #──O────────────────O─
                    #Validar si es un numero Positivo
                    if(int(_listaElementos[i][ini][j]) > 0 ):
                        #──O────────────────O─
                        #Quitar ceros a la izquierda
                        numero= int(_listaElementos[i][ini][j])
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
                    #Evaluar si esta vacio
                    txtprerequisito = _listaElementos[i][ini][j]
                    if (txtprerequisito == "" or txtprerequisito == " "):
                        None
                    else:
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
def validadorcursobligatorio(_listadoelementos,ini,nomeclatura,listacomparacion):
    try:
        #█═══════════════[ Validar si son numeros ] ══════════════════════════════════█
        Mensajevalidadorlistanumero = Bvalidadorlistadonumero(_listadoelementos,ini)
        #Validador
        if(Mensajevalidadorlistanumero != ""):
            #No son todos numeros
            mensaje0 = "Error en Codigo Curso Obligatorio. "+ Mensajevalidadorlistanumero
            VNT0.Mostrar(mensaje0)
            return False
        else:
            #──O────────────────O─
            #Son todos numeros
            #█═══════════════[ Validar la nomeclatura ] ══════════════════════════════════█
            #Validador si hay un listado de opciones correctas
            if(nomeclatura == True):
                mensaje2 = ""
                #──O────────────────O─
                #Validar la nomeclatura
                #Evaluar cada elemento
                for i in range(0,len(_listadoelementos)):
                    #──O────────────────O─
                    #Evaluar si es un numero del listado
                    numero = _listadoelementos[i][ini]
                    #Validador
                    banderaconcidencias = False
                    #Recorre la lista comparacion
                    for j in range(0,len(listacomparacion)):
                        #Evalua
                        if (numero == listacomparacion[j]):
                            banderaconcidencias = True
                            #para el ciclo for
                            break
                        else:
                            #La banera se queda en False
                            #No hubieron concidencias
                            None
                    #──O────────────────O─
                    # Validar si hubieron conciedencias    
                    if (banderaconcidencias == False):
                        mensaje2 += "linea " + str(i+1) +", "
                #──O────────────────O─
                #Validar si hay errores de concidencias en el listado
                if (mensaje2 != ""):
                    mensaje2 = "Error [Segmentador SEG2]: En codigo Obligatorio hay errores de codigo revisar las siguientes lineas: "+ mensaje2
                    VNT0.Mostrar(mensaje2)
                    return False
                else:
                    return True
                #──O────────────────O─
            else:
                #──O────────────────O─
                #No hay comparaciones
                return True
                #──O────────────────O─
        
    except Exception as e:
        VNT0.Mostrar("Error [Segmentador SEG2]: Ocurrio un error al validar si es obligatorio. \n"+str(e))




#————————————————————»✦«—————————————————————————————————————————————————##
#Boolean #Reusable
def Bvalidadorlistadonumeroopciones(_listadoelementos,ini,nomeclatura,listacomparacion,etiqueta):
    try:
        #█═══════════════[ Validar si son numeros ] ══════════════════════════════════█
        Mensajevalidadorlistanumero = Bvalidadorlistadonumero(_listadoelementos,ini)
        #Validador
        if(Mensajevalidadorlistanumero != ""):
            #No son todos numeros
            mensaje0 = "Error en Campo "+str(etiqueta)+". "+ Mensajevalidadorlistanumero
            VNT0.Mostrar(mensaje0)
            return False
        else:
            #──O────────────────O─
            #Son todos numeros
            #█═══════════════[ Validar la nomeclatura ] ══════════════════════════════════█
            #Validador si hay un listado de opciones correctas
            if(nomeclatura == True):
                mensaje2 = ""
                #──O────────────────O─
                #Validar la nomeclatura
                #Evaluar cada elemento
                for i in range(0,len(_listadoelementos)):
                    #──O────────────────O─
                    #Evaluar si es un numero del listado
                    numero = _listadoelementos[i][ini]
                    #Validador
                    banderaconcidencias = False
                    #Recorre la lista comparacion
                    for j in range(0,len(listacomparacion)):
                        #Evalua
                        if (numero == listacomparacion[j]):
                            banderaconcidencias = True
                            #para el ciclo for
                            break
                        else:
                            #La banera se queda en False
                            #No hubieron concidencias
                            None
                    #──O────────────────O─
                    # Validar si hubieron conciedencias    
                    if (banderaconcidencias == False):
                        mensaje2 += "linea " + str(i+1) +", "
                #──O────────────────O─
                #Validar si hay errores de concidencias en el listado
                if (mensaje2 != ""):
                    mensaje2 = "Error [Segmentador SEG2]: En el campo "+etiqueta+" hay errores de codigo revisar las siguientes lineas: "+ mensaje2
                    VNT0.Mostrar(mensaje2)
                    return False
                else:
                    return True
                #──O────────────────O─
            else:
                #──O────────────────O─
                #No hay comparaciones
                return True
                #──O────────────────O─
    except Exception as e:
        VNT0.Mostrar("Error [Segmentador SEG2]: Ocurrio un error al validar "+etiqueta+". \n"+str(e))
        return None



#————————————————————»✦«—————————————————————————————————————————————————##
#Boolean #Reusable
def Bvalidadornumero(textonum):
    try:
        numero = int(textonum)
        return True
    except Exception as e:
        return False
#————————————————————»✦«—————————————————————————————————————————————————##
#Boolean #Reusable
def Bvalidadorlistadonumero(listanum, ini):
    try:
        mensaje = ""
        #──O────────────────O─
        #Evaluar lista numero
        for i in range(0,len(listanum)):
            txtnumero = listanum[i][ini]
            #──O────────────────O─
            #Evaluar si es un numero
            try:
                numero = int(txtnumero)
            except:
                mensaje += "linea "+ str(i+1)+", " 
        #──O────────────────O─
        #Si hubo errores completar mensaje
        if (mensaje != ""):
            mensaje = "Error: hay valores que no son numeros en las siguiente Lineas: " + mensaje
        

        return mensaje
    except Exception as e:
        mensaje = "Error [Segmentador SEG2]: Ocurrio un error en Bvalidadorlistadonumero "
        return mensaje
    

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
        Validadorprereqisitos= validadorprerequisitos(listaElementos,2," prerequisitos")
        print("Validando Prerequisitos curso.... ",Validadorprereqisitos)
        #█═══════════════[ Validar Obligatorio ] ══════════════════════════════════█
        ValidadorObligatorio = validadorcursobligatorio(listaElementos,3,True,['0','1'])
        print("Validando Curso Obligatorio.... ",ValidadorObligatorio)
        #█═══════════════[ Validar Semestre ] ══════════════════════════════════█
        ValidadorSemestre = Bvalidadorlistadonumeroopciones(listaElementos,4,False,None,"SEMESTRE")
        print("Validando Semestre.... ", ValidadorSemestre)
        #█═══════════════[ Validar Creditos ] ══════════════════════════════════█
        ValidadorCreditos = Bvalidadorlistadonumeroopciones(listaElementos,5,False,None,"CREDITOS")
        print("Validando Creditos.... ", ValidadorCreditos)
        #█═══════════════[ Validar Estados ] ══════════════════════════════════█
        ValidadorEstados = Bvalidadorlistadonumeroopciones(listaElementos,6,True,['0','1','-1'],"ESTADOS")
        print("Validando Estados.... ", ValidadorEstados)
    
    #█═══════════════[ Validardor en General ] ══════════════════════════════════█ 
    if(Validadorcodigocurso == True and Validadorprereqisitos == True and ValidadorObligatorio == True and ValidadorSemestre == True and ValidadorCreditos == True and ValidadorEstados == True):
        #Si todo los campos estan bien 
        print("Archivo LFP Validado.")
        print("================================")
    else:
        print("Hubo un Error al cargar el archivo LFP porfavor corregir el error.")
    