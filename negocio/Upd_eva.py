import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def updat_eva(new_cal, new_ide, new_idma, idev):
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    # cone()
    # print('hello')
    parame = ''' UPDATE evaluacion SET calific = ?, idest = ?, idmat = ? WHERE ideva = ? '''
    data_tuple = (new_cal, new_ide, new_idma, idev)
    c.execute(parame, data_tuple)
    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

