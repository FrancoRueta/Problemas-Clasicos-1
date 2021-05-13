import logging
from random import randint
import time
from threading import Thread

# _______________________________________________________________________
# Imports

from threading  import Lock

# _______________________________________________________________________
# Class


class RWLock(object):
    # Constructor

    def __init__(self):

        self.w_lock = Lock()
        self.num_r_lock = Lock()
        self.num_r = 0 

    # Metodos de Lectura (Reading).

    def r_acquire(self):
        self.num_r_lock.acquire()
        self.num_r += 1
        if self.num_r == 1:
            self.w_lock.acquire()
        self.num_r_lock.release()

    def r_release(self):
        assert self.num_r > 0
        self.num_r_lock.acquire()
        self.num_r -= 1
        if self.num_r == 0:
            self.w_lock.release()
        self.num_r_lock.release()

    # Métodos de Escritura (Writing).

    def w_acquire(self):
        self.w_lock.acquire()

    def w_release(self):
        self.w_lock.release()


#-------------------------------------------------------------------------------//
#---------------------------------------------------------------------//



lockRW = RWLock()

partido = ["",0,"",0] 

equipos = ["Boca", "River", "Racing", "Independiente", "San Lorenzo", "Huracán", 
"Gimnasia", "Estudiantes", "Velez", "Ferro", "Lanus", "Quilmes"]

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)



def escritor(id):
    global partido          #Le damos partido y equipos a nuestro escritor.
    global equipos
    nombre = f"Escritor numero:{id}" #Nombre para mejor manejo.
    while True:
        nRandom1 = randint(0,len(equipos)-1)
        nRandom2= randint(0,len(equipos)-1)
        while nRandom1 == nRandom2:
            nRandom2 = randint(0,len(equipos)-1)
        lockRW.w_acquire()
        try:
            partido[0] = equipos[nRandom1]
            partido[1] = randint(0,3)
            partido[2] = equipos[nRandom2]
            partido[3] = randint(0,3)
            logging.info(f"{nombre} Actualizo el partido.")
        finally:
            lockRW.w_release()
            time.sleep(randint(1,2))

def lector(id):
    global partido
    global equipos
    nombre = f"Lector-{id}"
    while True:
        lockRW.r_acquire()
        try:
            logging.info(f"""{nombre}: El resultado fue: {partido[0]}:{partido[1]} - {partido[2]}:{partido[3]}""")
        finally:
            lockRW.r_release()
            time.sleep(randint(1,2))


def main():
    hilos = []
    for i in range(1):
        writer = Thread(target=escritor, args=(i,))
        logging.info(f"Arrancando escritor:{i}")
        writer.start()
        hilos.append(writer)
    for i in range(4):
        reader = Thread(target=lector,args=(i,))
        logging.info(f"Arrancando lector:{i}")
        reader.start()
        hilos.append(escritor)
    for thread in hilos:
        thread.join()

if __name__ == '__main__':
    main()