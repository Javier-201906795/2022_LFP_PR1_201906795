#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import pathlib
import LFP_VNT0_Errores as VNT0
import LFP_CRUD_DB as CRUD


#█┼┼┼┼┼┼┼┼┼┼┼[ VARIABLES GLOBLAES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█



#█┼┼┼┼┼┼┼┼┼┼┼[ FUNCIONES  ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
#————————————————————»✦«—————————————————————————————————————————————————#
def agregarcurso(ListaCurso):
    print("Agregando Curso.... ")
    # #█═══════════════[ obtener lista DB ] ══════════════════════════════════█
    # ListadoDB = CRUD.leerdb()
    # print(ListadoDB)
    #█═══════════════[ Convertir a CSV ] ══════════════════════════════════█ 
    print(ListaCurso)
    textoDB = obtenretextoDB()
    textocsv = textoacsv(ListaCurso)
    textoGrabarDB = textoDB  + textocsv
    print("texto csv: \n" + textoGrabarDB)
    #█═══════════════[ Agregar curso ] ══════════════════════════════════█ 
    

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