#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import LFP_VNT0_Errores as VNT0


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
global Texto
Texto = " "


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
def exportartexto(texto):
    #█═══════════════[ Separador Salto de Linea ] ══════════════════════════════════█
    #funcion que retorna un listado o un objeto vacio
    listadoSaltosLinea= separadorlineas(texto)
    print("test1: ",listadoSaltosLinea,"\n")
    
    #█═══════════════[ Separador comas ] ══════════════════════════════════█
    #funcion que retorna un listado o un objeto vacio
    listadoComas = separadorcomas(listadoSaltosLinea)
    print("test2:", listadoComas,"\n")
    print("test2.1: ",listadoComas[11][2],"\n")

    # global lista1
    # lista1 = []
    # #──O────────────────O─
    # for i in range(0,(len(listadoSaltosLinea))):
    #     #──O────────────────O─
    #     #Separar por ,
    #     lista1.append(listadoSaltosLinea[i].split(","))
        #──O────────────────O─
#        print(lista1[i])
#        print("================================")
#        print(lista1)
#        print("================================")
#        print(lista1[0][1])
#        print(lista1[11][2])




#     #█═══════════════[ Separador de punto y coma ] ══════════════════════════════════█
#     # separador para los cursos prerequisitos
#     #──O────────────────O─
#     for i in range(0,(len(listadoSaltosLinea))):
#         #──O────────────────O─
#         #Separar por ; y lo guarda en la lista 
#         #print(lista1[i][2])
#         lista1[i][2] = lista1[i][2].split(";")
#         #──O────────────────O─
# #        print(lista1[11][2])
# #        print(lista1[11][2][0])
# #        print(lista1[11][2][1])
    

#     print(lista1)