#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
global Texto
Texto = " "


#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
def exportartexto(texto):
    #█═══════════════[ Separador Salto de Linea ] ══════════════════════════════════█
    #se dividira el texto en los saltos de linea
    listadoSaltosLinea=texto.splitlines()
    print("lita0: ", len(listadoSaltosLinea))
    #█═══════════════[ Separador comas ] ══════════════════════════════════█
    #se guardara una sublistas con los elemnetos que esten antes de la coma
    global lista1
    lista1 = []
    print("lista1: ", len(lista1))
    #──O────────────────O─
    for i in range(0,(len(listadoSaltosLinea))):
        #──O────────────────O─
        #Separar por ,
        lista1.append(listadoSaltosLinea[i].split(","))
        #──O────────────────O─
#        print(lista1[i])
#        print("================================")
#        print(lista1)
#        print("================================")
#        print(lista1[0][1])
#        print(lista1[11][2])

    #█═══════════════[ Separador de punto y coma ] ══════════════════════════════════█
    # separador para los cursos prerequisitos
    #──O────────────────O─
    for i in range(0,(len(listadoSaltosLinea))):
        #──O────────────────O─
        #Separar por ; y lo guarda en la lista 
        #print(lista1[i][2])
        lista1[i][2] = lista1[i][2].split(";")
        #──O────────────────O─
        
#        print(lista1[11][2])
#        print(lista1[11][2][0])
#        print(lista1[11][2][1])
    

    print("Evaluando")