import threading
import random
import logging
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class listaFinita(list):

    def __init__(self, max_elementos):
            self.max_elementos = max_elementos
            super().__init__()
            self.condicion = threading.Condition()

    def pop(self,index = 0): #Agregamos el modulo condition.
        self.condicion.acquire()
        while len(self) == 0:
            self.condicion.wait()
        elemento = super().pop(index)
        self.condicion.notify(1)
        self.condicion.release()
        return elemento

    def append(self, item): #Agregamos el modulo condition.
        self.condicion.acquire()
        while len(self) == self.max_elementos:
            self.condicion.wait()
        super().append(item)
        self.condicion.notify(1)
        self.condicion.release()

    def insert(self, index, item):
        assert index < self.max_elementos, "indice invalido"
        super().insert(index, item)

    def full(self):
        if len(self) == self.max_elementos:
            return True
        else:
            return False



class Productor(threading.Thread):
    def __init__(self, lista = listaFinita, elementosAppendeables= [("España","Madrid"), ("Francia","Paris"),("Italia","Roma"),("Inglaterra","Londres"),("Alemania","Berlin"),("Rusia","Moscu"),
("Turquia","Istambul"),("China","Pekin"), ("Japon","Tokio"),("Emiratos Arabes","Dubai"),("Argentina","Buenos Aires"),
("Brasil","Brasilia"),("Colombia","Bogota"),("Uruguay","Montevideo")]):
        super().__init__()
        self.lista = lista
        self.elementosAppendeables = elementosAppendeables

    
    
    def run(self):
        while True:
            self.lista.append(random.choice(self.elementosAppendeables))
            #logging.info(f'Produjo: {self.lista[-1]}')
            time.sleep(random.randint(1,5))


class Consumidor(threading.Thread):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista


    def run(self):
        while True:
            elemento = self.lista.pop()
            logging.info(f'La capital de {elemento[0]} es {elemento[1]}')
            time.sleep(random.randint(1,5))

def main():
    hilos = []
    lista = listaFinita(4)

    for i in range(4):
        productor = Productor(lista)
        consumidor = Consumidor(lista)
        hilos.append(productor)
        hilos.append(consumidor)

        logging.info(f'Arrancando productor {productor.name}')
        productor.start()

        logging.info(f'Arrancando consumidor {consumidor.name}')
        consumidor.start()

    for h in hilos:
        h.join()


if __name__ == '__main__':
    main()
