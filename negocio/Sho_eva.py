import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def showEva():
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    c.execute(''' SELECT  ideva, estudiante.nomest, materia.nommat, calific
        FROM evaluacion
        INNER JOIN estudiante
        ON evaluacion.idest = estudiante.idest
        INNER JOIN materia
        ON evaluacion.idmat = materia.idmat; ''')

    rows = c.fetchall()

    for row in rows:
        print(row)

    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

