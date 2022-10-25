import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def inser_est(nomes,matric):
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    # cone()
    # print('hello')
    parame = ''' INSERT INTO estudiante 
            (nomest, matri) 
            VALUES (?, ?); '''
    data_tuple = (nomes, matric)
    c.execute(parame, data_tuple)
    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

