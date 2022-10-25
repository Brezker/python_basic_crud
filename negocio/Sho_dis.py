import sys
import sqlite3
# here you have to put your path app folder
sys.path.insert(1,'/home/jul/codes/julian/')
from datos.conexBD import *

def showDis(ides):
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('hola')

    # cone()
    # print('hello')
    parame = ''' SELECT
    IIF((SELECT AVG(calific)
        FROM evaluacion
        INNER JOIN estudiante
        ON evaluacion.idest = estudiante.idest
        WHERE estudiante.idest = :id) > 9.7, '40% Off',
        IIF((SELECT AVG(calific)
            FROM evaluacion
            INNER JOIN estudiante
            ON evaluacion.idest = estudiante.idest
            WHERE estudiante.idest = :id) > 9.5, '25% Off',
            IIF((SELECT AVG(calific)
                FROM evaluacion
                INNER JOIN estudiante
                ON evaluacion.idest = estudiante.idest
                WHERE estudiante.idest = :id) > 9.1, '15% Off','No discout disponible')
        )
    ) '''
    # data_tuple = (ides)
    c.execute(parame, {"id": ides})
    
    rows = c.fetchone()

    print(rows)

    quer = ''' SELECT AVG(calific) AS prom
        FROM evaluacion
        INNER JOIN estudiante
        ON evaluacion.idest = estudiante.idest
        WHERE estudiante.idest = :id '''
    # data_tuple = (ides)
    c.execute(quer, {"id": ides})
    
    res = c.fetchone()

    print("For your "+str(res)+" grade averange.") 

    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

