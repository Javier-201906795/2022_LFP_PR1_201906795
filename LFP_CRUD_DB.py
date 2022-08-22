#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import pathlib
import LFP_VNT0_Errores as VNT0


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#————————————————————»✦«—————————————————————————————————————————————————#
def cargamasiva(listaElementos):
    try:
        print("CRUD | cargamasiva : Evaluando....")
        #█═══════════════[ Guardar en Variable Global ] ══════════════════════════════════█ 
        global ListadoElementos
        ListadoElementos = listaElementos
        #█═══════════════[ Compara Cursos actuales vs carga masiva ] ══════════════════════════════════█ 
        #Evalua que no se repitan los cursos
        #──O────────────────O─
        #Carga la DB en un listado 
        ListadoDB = leerdb()
        if (ListadoDB == []):
            print("DB vacio.")
            #█═══════════════[ Unir listas ] ══════════════════════════════════█ 
            #Unir listas
            ListadoDB.extend(ListadoElementos)
            #█═══════════════[ Guardar en Base de Datos ] ══════════════════════════════════█ 
            # #Guarda la informacion en un archivo CSV 
            textocsv = convertirlistaacsv(ListadoDB)
            print("TextoCSV: ")
            print(textocsv)
            
            escribirDB(textocsv)

        else:
            #──O────────────────O─
            #Comprar listados en busquedad de concidencias codigo
            Listacondiencias = comparadorconcidencias(ListadoDB,ListadoElementos,0)
    #        print(Listacondiencias)
            #──O────────────────O─
            #Evaluar
            if (Listacondiencias != []) :
                print("Se encontraron condidencias, sobrescribiendo DB.")

                #──O────────────────O─
                #Sobre escribe los valores repetidos
                #──O────────────────O─
                #Nueva lista
                templist = []
                for i in range(0,len(ListadoElementos)):
                    templist.append(ListadoElementos[i])
                #──O────────────────O─
                contador = -1
                for i in range(0,len(Listacondiencias)):
                    #print("DB: ", ListadoDB[Listacondiencias[i][0]])
                    #print("E: ", ListadoElementos[Listacondiencias[i][1]])
                    ListadoDB[Listacondiencias[i][0]] = ListadoElementos[Listacondiencias[i][1]]
                    #print("DBnew: ", ListadoDB[Listacondiencias[i][0]])
                    
                    #──O────────────────O─
                    #Elimina el elemento repetido
                    #print("Elemento a eleminar: ", Listacondiencias[i][1] )
                    contador += 1
                    if (contador < 1):
                        templist.pop(Listacondiencias[i][1])
                    else:
                        templist.pop(Listacondiencias[i][1] - contador)
                        
                    
                    
                    
                    

                #█═══════════════[ Unir listas ] ══════════════════════════════════█ 
                #Unir listas
                ListadoDB.extend(templist)
                

            else:
                print("No se encontraron concidencias.")
                #█═══════════════[ Unir listas ] ══════════════════════════════════█
                ListadoDB.extend(ListadoElementos)

            #█═══════════════[ Guardar en Base de Datos ] ══════════════════════════════════█ 
            # #Guarda la informacion en un archivo CSV 
            textocsv = convertirlistaacsv(ListadoDB)
            print("TextoCSV: ")
            print(textocsv)
            
            escribirDB(textocsv)

        
    except Exception as e:
        VNT0.Mostrar("Error [CRUD]: Ocurrio un error en la carga masiva. \n"+e)

#————————————————————»✦«—————————————————————————————————————————————————#
def borrartodoDB():
    try:
        print("Borrando  DB....")
        #──O────────────────O─
        #Buscar ruta del fichero
        Ruta = pathlib.Path(__file__).parent.absolute()
        txtRuta = str(Ruta)
        txtRutaDB = txtRuta + "\LFP_DB.csv"
        #──O────────────────O─
        #Abrir el archivo
        archivocsv = open(txtRutaDB, "w", encoding="utf-8")
        #──O────────────────O─
        #Guardar
        archivocsv.write("")
        return True
    except Exception as e:
        print(e)
        return False

#————————————————————»✦«—————————————————————————————————————————————————#
def escribirDB(textonuevo):
    try:
        print("Escribiendo nuevo DB tipo csv.")
        #──O────────────────O─
        #Buscar ruta del fichero
        Ruta = pathlib.Path(__file__).parent.absolute()
        txtRuta = str(Ruta)
        txtRutaDB = txtRuta + "\LFP_DB.csv"
        #──O────────────────O─
        #Abrir el archivo
        archivocsv1 = open(txtRutaDB, "r", encoding="utf-8")
        archivocsv = open(txtRutaDB, "w", encoding="utf-8")
        #──O────────────────O─
        #Guardar
        textoanterior = archivocsv1.read()
        textonuevo = textoanterior + textonuevo
        archivocsv.write(textonuevo)
        # CERRAR ARCHIVO
        archivocsv.close()
        print("DB escrito correctamente.")

    except Exception as e:
        print("Erorr al guardar DB. \n"+e)
#————————————————————»✦«—————————————————————————————————————————————————#
def leerdb():
    try:
        print("Leyendo DB....")
        #──O────────────────O─
        #Buscar ruta del fichero
        Ruta = pathlib.Path(__file__).parent.absolute()
        txtRuta = str(Ruta)
        txtRutaDB = txtRuta + "\LFP_DB.csv"
        #──O────────────────O─
        #Abrir el archivo
        archivocsv = open(txtRutaDB, "r", encoding="utf-8")
        #──O────────────────O─
        #Leer archivo csv
        #crea un listado con cada linea 
        listacsv = archivocsv.readlines()

        # CERRAR ARCHIVO
        archivocsv.close()
        #──O────────────────O─
        #quitar saltos de lineas
        for i in range(0,len(listacsv)):
            temp = listacsv[i]
            #quita el salto de linea
            listacsv[i]= temp.rstrip()
        #──O────────────────O─
        #Separa comas (,)
        for i in range(0, len(listacsv)):
            temp = listacsv[i]
            #lo guarda en un segundo listado
            listacsv[i] = listacsv[i].split(",")
        #──O────────────────O─
        #Separa punto y comas (;)
        for i in range(0,len(listacsv)):
            temp = listacsv[i][2]
            listtemp = temp.split(";")
            listacsv[i][2] = listtemp

        print("OK")
        return listacsv



    except Exception as e:
        print("Error [CRUD]: Ocurrio un error al leer DB. \n"+e)
        return None



#————————————————————»✦«—————————————————————————————————————————————————#
def comparadorconcidencias(lista1,lista2,ini):
    #lista origianl vs lista comparada
    try:
        print("Buscando concidencias codigo.... ")
        #──O────────────────O─
        #Evalua los elementos de la lista 1 con los de la lista 2
        Bconcidencias = False
        listaconcidencias = []
        for i in range(0,len(lista1)):
            datoacomparar = lista1[i][ini]
            #──O────────────────O─
            #Evalua con todo los elementos de la lista 2
            for j in range(0,len(lista2)):
                #Evaluar si son iguales
                if (datoacomparar == lista2[j][ini]):
                    #──O────────────────O─
                    #Si hay concidencias 
                    #Marcar posicion
                    listaconcidencias.append([i,j])
                    #Validador
                    Bconcidencias = True
                else:
                    None
            #──O────────────────O─
        #──O────────────────O─
        #Evaluar si hay concidencias
        if (Bconcidencias == True):
            #Si hay concidencias
            #regresa el listado concidencias
            return listaconcidencias
        else:
            return None
    except Exception as e:
        print("Error [CRUD]: Ocurrio un error en comparadorconcidencias. \n"+e)
        return None
    
#————————————————————»✦«—————————————————————————————————————————————————#
def convertirlistaacsv(lista):
    try:
        print("Convirtiendo listado a texto...")
        #Colocar elementos coma
        txtnuevo = ""
        #recorre linea
        #──O────────────────O─
        for i in range(0,len(lista)):
            #recorre subelementos
            #──O────────────────O─
            for j in range(0,len(lista[i])):
                
                if (j == (len(lista[i])-1)):
                    #coloca final
                    txtnuevo += str(lista[i][j]) 
                elif (j == 2):
                    #coloca punto y coma
                    #ciclo for para sacar del listado
                    txttemplist = ""
                    
                    #──O────────────────O─
                    #Si el texto es cursos de prerequisitos
                    #print(len(lista[i][2]))
                    if (len(lista[i][2]) != 0):
                        #──O────────────────O─
                        for k in range(0,len(lista[i][2])):
                            #Evaluar si es el ultimo valor para no poner putno y coma
                            if (k == (len(lista[i][2]) - 1)):
                                txttemplist += str(lista[i][2][k]) + ","
                            else:    
                                txttemplist += str(lista[i][2][k]) + ";"
                        #──O────────────────O─
                        #agrega el listado
                        #print("txttemplist: ", txttemplist)
                        txtnuevo += txttemplist
                    else:
                        #no hay cursos de prerequisitos
                        txtnuevo += ","
                else:
                    #coloca comas
                    txtnuevo += str(lista[i][j]) + ","
            #──O────────────────O─
            txtnuevo += "\n" 
        #──O────────────────O─

        return txtnuevo

    except Exception as e:
        print("Error al convertir lista a csv. \n"+e)
        return ""