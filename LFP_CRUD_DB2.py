#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import pathlib
import LFP_VNT0_Errores as VNT0
import LFP_CRUD_DB as CRUD


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#————————————————————»✦«—————————————————————————————————————————————————#
def agregarcurso(ListaCurso):
    print("Agregando Curso.... ")
    
    #█═══════════════[ Convertir a CSV ] ══════════════════════════════════█ 
    print(ListaCurso)
    textoDB = obtenretextoDB()
    textocsv = textoacsv(ListaCurso)
    textoGrabarDB = textoDB  + textocsv + "\n"
    print("texto csv: \n" + textoGrabarDB)
    #█═══════════════[ Agregar curso ] ══════════════════════════════════█ 
    CRUD.escribirDB(textoGrabarDB)

#————————————————————»✦«—————————————————————————————————————————————————#
def obtenretextoDB():
    try:
        print("Obtener texto DB....")
        txtRutaDB = obtenerruta()
        #Abrir el archivo
        archivocsv = open(txtRutaDB, "r", encoding="utf-8")
        #LEER ARCHIVO 
        textoDB = archivocsv.read()
        return textoDB
    except Exception as e:
        print(e)
#————————————————————»✦«—————————————————————————————————————————————————#

#————————————————————»✦«—————————————————————————————————————————————————#
def obtenerruta():
    try:
        #──O────────────────O─
        #Buscar ruta del fichero
        Ruta = pathlib.Path(__file__).parent.absolute()
        txtRuta = str(Ruta)
        txtRutaDB = txtRuta + "\LFP_DB.csv"
        #──O────────────────O─
        return txtRutaDB
    except Exception as e:
        print(e)
        return None
    
#————————————————————»✦«—————————————————————————————————————————————————#
def textoacsv(Lista):
    try:
        print("Convertir texto a csv.... ")
        textocsv = ""
        for i in range(0,len(Lista)):
            if (i == (len(Lista) - 1)):
                textocsv += Lista[i]
            else:
                textocsv += Lista[i] + ","
        return textocsv

    except Exception as e:
        print(e)

#————————————————————»✦«—————————————————————————————————————————————————#
def Bbuscar(codigo):
    try:
        #█═══════════════[ obtener lista DB ] ══════════════════════════════════█
        ListadoDB = CRUD.leerdb()
        print(ListadoDB)
        print(len(ListadoDB))
        print("Codigo a buscar: ", codigo)
        #█═══════════════[ Buscar si existe el codigo ] ══════════════════════════════════█
        encontrado = False
        posicion = -1
        for i in range(0,len(ListadoDB)):
            print(int(ListadoDB[i][0]))
            #Evaluar
            if (int(ListadoDB[i][0]) == int(codigo)):
                print("Encontrado.")
                encontrado = True
                posicion = i + 1
            
        if (encontrado == True):
            return posicion
        else:
            return False

    except Exception as e:
        print(e)
        return False