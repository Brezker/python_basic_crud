import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def showEst():
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    c.execute(''' SELECT * FROM estudiante ''')

    rows = c.fetchall()

    for row in rows:
        print(row)

    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

