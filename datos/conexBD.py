import sqlite3

# class cone():
#     con = sqlite3.connect('datos/julianbd')
#     c = con.cursor()
#     print('hola')

def table():
    # return cone()
    con = sqlite3.connect('datos/julianbd')
    c = con.cursor()
    # print('creating')
    #Check if table estudiante exist, if not create it
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='estudiante' ''')
    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : {
    	print('Table estudiante already exists.')
    }
    else:
        c.execute(''' CREATE TABLE estudiante (
            idest INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            nomest VARCHAR (50) NOT NULL, 
            matri BIGINT (10) UNIQUE NOT NULL
        ) ''')
        print('Table estudiante created correctly.')
    #commit the changes to db
    con.commit()

    #Check if table materia exist, if not create it
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='materia' ''')
    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : {
    	print('Table materia already exists.')
    }
    else:
        c.execute(''' CREATE TABLE materia (
            idmat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            nommat VARCHAR (50) UNIQUE NOT NULL
        ) ''')
        print('Table materia created correctly.')
    #commit the changes to db
    con.commit()

    #Check if table evaluacion exist, if not create it
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='evaluacion' ''')
    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : {
    	print('Table evaluacion already exists.')
    }
    else:
        c.execute(''' CREATE TABLE evaluacion (
            ideva INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            idest INTEGER REFERENCES estudiante (idest) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, 
            idmat INTEGER REFERENCES materia (idmat) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
            calific DECIMAL NOT NULL
        ) ''')
        print('Table evaluacion created correctly.')
    #commit the changes to db
    con.commit()

    #close the connection
    con.close()

