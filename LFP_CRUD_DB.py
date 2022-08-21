#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import LFP_VNT0_Errores as VNT0


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#————————————————————»✦«—————————————————————————————————————————————————#
def cargamasiva(listaElementos):
    try:
        print("CRUD | cargamasiva : Evaluando....")
        #█═══════════════[ Guardar en Variable Global ] ══════════════════════════════════█ 
        global ListadoElemento
        ListadoElemento = listaElementos
        #█═══════════════[ Compara Cursos actuales vs carga masiva ] ══════════════════════════════════█ 
        #Evalua que no se repitan los cursos
        #──O────────────────O─
        #Carga la DB en un listado 

        #█═══════════════[ Guardar en Base de Datos ] ══════════════════════════════════█ 
        #Guarda la informacion en un archivo CSV 

        
    except Exception as e:
        VNT0.Mostrar("Error [CRUD]: Ocurrio un error en la carga masiva. \n"+e)
    
#————————————————————»✦«—————————————————————————————————————————————————#
def comparadorconcidencias(lista1,lista2,ini):
    #lista origianl vs lista comparada
    try:
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
                    listaconcidencias.append(j)
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
    