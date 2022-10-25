import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def updat_mat(new_nom, idma):
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    # cone()
    # print('hello')
    parame = ''' UPDATE materia SET nommat = ? WHERE idmat = ? '''
    data_tuple = (new_nom, idma)
    c.execute(parame, data_tuple)
    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

