# guardarCocheDB no es responsabilidad de la clase 'Coche'

class Coche:
    def __init__(self, marca):
        self.marca = marca

    def getMarcaCoche(self):
        return self.marca

class CocheDB:
    def guardarCocheDB(self, coche):
        pass

    def eliminarCocheDB(self, coche):
        pass
