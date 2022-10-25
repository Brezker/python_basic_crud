import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def delet_mat(ides):
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    # cone()
    # print('hello')
    parame = ''' DELETE FROM materia WHERE idmat= :id '''
    # data_tuple = (ides)
    c.execute(parame, {"id": ides})
    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

