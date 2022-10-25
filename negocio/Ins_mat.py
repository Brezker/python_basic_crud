import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def inser_mat(nomat):
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    # cone()
    # print('hello')
    parame = ''' INSERT INTO materia 
            (nommat) 
            VALUES (:nom); '''
    # data_tuple = (nomes)
    c.execute(parame, {"nom": nomat})
    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

