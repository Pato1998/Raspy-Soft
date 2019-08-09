import MySQLdb
from config import env

class Conexion:
    #Constructor (inicia la conexion)
    def __init__(self):        
        self.conn = MySQLdb.connect(env.host, env.user, env.password, env.db)
    
    #Metodo para cerrar la conexion
    
    #Otros


    