from Class.DbBase import DbBase

class Eventos(DbBase):
    def __init__(self):
        DbBase.__init__(self)
        
    def registrarEntrada(self, id, tipo):
        return 'ok'
        
    def registrarSalida(self, id, tipo):
        pass

    def verEntradas(self):
        self.show('ENTRADAS')

    def verSalidas(self):
        self.show('SALIDAS')
