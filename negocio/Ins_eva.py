import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def inser_eva(ide,idm,cal):
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    # cone()
    # print('hello')
    parame = ''' INSERT INTO evaluacion 
            (idest, idmat, calific) 
            VALUES (?, ?, ?); '''
    data_tuple = (ide, idm, cal)
    c.execute(parame, data_tuple)
    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

