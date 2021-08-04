from abc import ABC, abstractmethod

# Cuando necesitemos añadir otro coche de otra marca, vamos a tener que modificar la función.

class Coche(ABC):
    @abstractmethod
    def precioMedioCoche(self):
        pass

class Renault(Coche):
    def precioMedioCoche(self):
        return 18000

class Audi(Coche):
    def precioMedioCoche(self):
        return 25000


class Mercedes(Coche):
    def precioMedioCoche(self):
        return 27000

def imprimirPrecioMedioCoche(arrayCoches):
    for coche in arrayCoches:
        print(coche.precioMedioCoche())

if __name__ == "__main__":
    arrayCoches = [
            Renault(),
            Audi(),
            Mercedes()]
    imprimirPrecioMedioCoche(arrayCoches)


