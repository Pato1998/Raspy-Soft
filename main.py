from Class.Eventos import Eventos
from Class.Sfx import Sfx
from config.env import TIMEOUT
#ID, LECTOR
#DNI: 1, RFID: 2
lector = -1
msg = '' 

sfx = Sfx()
sfx.start() 

#A modo de prueba!
id = input('Identificacion: ')
lector = input('lector: ')


if lector == 1:
    print '1'
    #Extraer numero de dni
    #Solo sean numeros, sino retornar msg
elif lector == 2:
    print '2'
    #Validar que sea un numero longitu 11
    #sino retornar msg
elif lector == 3:
    Eventos = Eventos()
    Eventos.verEntradas()
    exit()


#Si msg no esta vacio, mostrar msg

if msg == '':
    Eventos = Eventos()
    msg = Eventos.registrarEntrada(id, lector)
    print msg
else:
    print msg