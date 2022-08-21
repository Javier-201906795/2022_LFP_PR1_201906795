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
#        print(ListadoDB)
        #──O────────────────O─
        #Comprar listados en busquedad de concidencias codigo
        Listacondiencias = comparadorconcidencias(ListadoDB,ListadoElementos,0)
#        print(Listacondiencias)
        #──O────────────────O─
        #sobre escribe los valores repetidos


        #█═══════════════[ Guardar en Base de Datos ] ══════════════════════════════════█ 
        #Guarda la informacion en un archivo CSV 


        
    except Exception as e:
        VNT0.Mostrar("Error [CRUD]: Ocurrio un error en la carga masiva. \n"+e)

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
    