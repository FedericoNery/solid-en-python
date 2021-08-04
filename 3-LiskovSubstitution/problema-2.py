class Coche:
    def __init__(self, marca):
        self.marca = marca

    def getMarcaCoche(self):
        return self.marca

class Renault(Coche):
    def numAsientosRenault(self):
        pass

class Audi(Coche):
    def numAsientosAudi(self):
        pass

class Mercedes(Coche):
    def numAsientosMercedes(self):
        pass

class Ford(Coche):
    def numAsientosFord(self):
        pass

"""def imprimirNumAsientos(arrayCoches):
    for coche in arrayCoches:
        if(coche instanceof Renault):
            print(numAsientosRenault(coche))
        if(coche instanceof Audi):
            print(numAsientosAudi(coche))
        if(coche instanceof Mercedes):
            print(numAsientosMercedes(coche))"""

#imprimirNumAsientos(arrayCoches)

#Si añadimos un nuevo coche
arrayCoches = [
        Renault(),
        Audi(),
        Mercedes(),
        Ford()]

def imprimirNumAsientos(arrayCoches):
    for coche in arrayCoches:
        if isinstance(coche,Renault):
            print(coche.numAsientosRenault())

        if isinstance(coche, Audi):
            print(coche.numAsientosAudi())

        if isinstance(coche,Mercedes):
            print(coche.numAsientosMercedes())

        if isinstance(coche, Ford):
            print(coche.numAsientosFord())

imprimirNumAsientos(arrayCoches)