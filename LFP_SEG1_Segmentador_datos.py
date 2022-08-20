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
    #█═══════════════[ Separador ] ══════════════════════════════════█
    global lista1
    lista1 = []
    print("lista1: ", len(lista1))
    #──O────────────────O─
    for i in range(0,(len(listadoSaltosLinea))):
        print("numreo:",i)
        #──O────────────────O─
        #Separ por ,
        lista1.append(listadoSaltosLinea[i].split(","))
        print(lista1[i])
    
    print("================================")
    print(lista1)
    print("================================")
    print(lista1[0][1])
    print(lista1[11][2])

    print("Evaluando")