from abc import ABC, abstractmethod

def imprimirNumAsientos(arrayCoches):
        for coche in arrayCoches:
            print(coche.numAsientos())

#imprimirNumAsientos(arrayCoches);

class Coche(ABC):
    @abstractmethod
    def numAsientos(self):
        pass


class Renault(Coche):
    def numAsientos(self):
        return 5