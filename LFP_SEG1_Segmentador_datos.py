#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
global Texto
Texto = " "


#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
def exportartexto(texto):
    #█═══════════════[ Separador Salto de Linea ] ══════════════════════════════════█
    #se dividira el texto en los saltos de linea
    listadoSaltosLinea=texto.splitlines()
    #█═══════════════[ Separador ] ══════════════════════════════════█
    global lista1
    #──O────────────────O─
    for i in range(0,(len(listadoSaltosLinea)-1)):
        #──O────────────────O─
        #Separ por ,
        lista1 = listadoSaltosLinea[i]
        print("hi")
    

    print("Evaluando")