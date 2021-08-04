class Coche:
    def __init__(self, marca):
        self.marca = marca

    def getMarcaCoche(self):
        return self.marca


def imprimirPrecioMedioCoche(arrayCoches):
    for coche in arrayCoches:
        if(coche.marca.equals("Renault")):
            print(18000)
        if(coche.marca.equals("Audi")):
            print(25000)

if __name__ == "__main__":
    arrayCoches = [Coche("Renault"), Coche("Audi")]
    imprimirPrecioMedioCoche(arrayCoches)


arrayCoches = [
    Coche("Renault"),
    Coche("Audi"),
    Coche("Mercedes")]

def imprimirPrecioMedioCoche(arrayCoches):
    for coche in arrayCoches:
        if(coche.marca.equals("Renault")):
            print(18000)
        if(coche.marca.equals("Audi")):
            print(25000)
        if(coche.marca.equals("Mercedes")):
            print(27000)
