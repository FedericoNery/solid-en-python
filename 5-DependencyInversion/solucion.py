from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def accelerate(self):
        pass

class RacingCar(Car):
    def __init__(self, fuel):
        self.remainingFuel = fuel
        self.power = 0

    def accelerate(self):
        self.power += 1
        self.remainingFuel -= 1

class Driver():
    def __init__(self, racingCar):
        self.racingCar = racingCar

    def increaseSpeed(self):
        self.racingCar.accelerate()


"""
En el ejemplo tenemos la clase Driver que tiene una dependencia con la clase RacingCar ya que en su constructor se instancia un objeto de la clase RacingCar:

Para introducir una abstracción que desacople ambas clases creamos la interfaz Car de forma que la clase Driver en su constructor 
recibirá un objeto que implementa dicha interfaz. En el ejemplo la clase RacingCar implementa dicha interfaz pero si hemos aplicado 
correctamente los otros principios podremos utilizar otras implementaciones y ampliar la funcionalidad del sistema sin que se produzcan errores.

Este principio está relacionado con el concepto de "Inyección de Dependencias" ya que será otro sistema el que 'inyecte' 
en tiempo de ejecución la implementación que requiera la clase en el constructor.

"""