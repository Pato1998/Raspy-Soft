from Class.Conexion import Conexion

#Metodos base
#Consultas select, inserts, ejecucion de sp

class DbBase(Conexion):

    def __init__(self):
        Conexion.__init__(self)

    def show(self, table):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM " + table)
        
        print cur.fetchall()
        #for row in cur.fetchall():
        #    print row

    #Ejecutar Stored Procedure
    #Debe recibir: Nombre del sp, y parametros
    def execSP(self):
        cur = self.conn.cursor()
        p = cur.execute("call prueba(202020202020)")
        return cur.fetchall()       
