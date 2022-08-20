#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import LFP_VNT0_Errores as VNT0
import LFP_SEG2_Validadores as SEG2


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#————————————————————»✦«—————————————————————————————————————————————————#
def separadorlineas(texto):
    try:
        #──O────────────────O─
        #se dividira el texto en los saltos de linea
        listanueva = texto.splitlines()
        #──O────────────────O─
        return listanueva
        #──O────────────────O─
    except Exception as e:
        VNT0.Mostrar("Error [Segmentador SEG1]: Ocurrio un error con el texto ingresado, problema con el salto de linea. \n " + str(e))
        return None

#————————————————————»✦«—————————————————————————————————————————————————#
def separadorcomas(lista):
    #se guardara una sublistas con los elemnetos que esten antes de la coma
    try:
        #──O────────────────O─
        listanueva2 = []
        #──O────────────────O─
        #crea lista separadas por las coma y las guarda en un nuevo listado
        for i in range(0,(len(lista))):
            #──O────────────────O─
            listanueva2.append(lista[i].split(","))
        
        #──O────────────────O─
        #regresa la lista modificada
        return listanueva2
        #──O────────────────O─

    except Exception as e:
        VNT0.Mostrar("Error [Segmentador SEG1]: Ocurrio un error con el texto ingresado, problema con el separado ',' (coma) \n " + str(e))
        return None

#————————————————————»✦«—————————————————————————————————————————————————#
def separadorpuntoycoma(lista):
    try:
        #──O────────────────O─
        #crea una sublista (separador  ;)
        for i in range(0,(len(lista))):
            #──O────────────────O─
            lista[i][2] = lista[i][2].split(";")
        #──O────────────────O─
        return lista
        #──O────────────────O─
    except Exception as e:
        VNT0.Mostrar("Error [Segmentador SEG1]: Ocurrio un error con el texto ingresado, problema con el separado ';' (punto y coma) \n " + str(e))
        return None


#————————————————————»✦«—————————————————————————————————————————————————#
def exportartexto(texto):
    #█═══════════════[ Separador Salto de Linea ] ══════════════════════════════════█
    #funcion que retorna un listado o un objeto vacio
    listadoSaltosLinea= separadorlineas(texto)
    # print("test1: ",listadoSaltosLinea,"\n")
    
    #█═══════════════[ Separador comas ] ══════════════════════════════════█
    #──O────────────────O─
    #Validador 1
    if (listadoSaltosLinea != None):
        #funcion que retorna un listado o un objeto vacio
        listadoComas = separadorcomas(listadoSaltosLinea)
        # print("test2:", listadoComas,"\n")
        # print("test2.1: ",listadoComas[11][2],"\n")

    #█═══════════════[ Separador de punto y coma ] ══════════════════════════════════█
    #──O────────────────O─
    #Validador 2
    if (listadoSaltosLinea != None and listadoComas != None):
        listaElementos = separadorpuntoycoma(listadoComas)
        # print("test3: ", listaElementos)

    #█═══════════════[ Exportar a Validadores SEG2 ] ══════════════════════════════════█
    #──O────────────────O─
    #Validador 3
    if (listadoSaltosLinea != None and listadoComas != None and listaElementos != None):
        SEG2.exportarValidadores(listaElementos)
