from abc import ABC, abstractmethod

class EngineSwitch(ABC):
    @abstractmethod
    def startEngine(self):
        pass

class CameraSwitch(EngineSwitch):
    @abstractmethod
    def turnCameraOn(self):
        pass

    @abstractmethod
    def turnCameraOff(self):
        pass

class RadioSwitch(EngineSwitch):
    @abstractmethod
    def turnRadioOn(self):
        pass

    @abstractmethod
    def turnRadioOff(self):
        pass

class Car(RadioSwitch):

    def __init__(self):
        self._radioOn = None

    def startEngine(self):
        pass

    def turnRadioOn(self):
        self._radioOn = True

    def turnRadioOff(self):
        self._radioOn = False

class Drone(CameraSwitch):

    def __init__(self):
        self._cameraOn = None

    def startEngine(self):
        pass

    def turnCameraOn(self):
        self._cameraOn = True

    def turnCameraOff(self):
        self._cameraOn = False

"""
En el ejemplo tenemos las subclases Drone y Car que implementan la interfaz Switches.

En este ejemplo las subclases, debido a la herencia, se ven obligadas a implementar con un cuerpo vacío los métodos que no les son necesarios. 
La subclase Car se ve obligada a implementar los métodos turnCameraOn() y turnCameraOff() que son más propios de la subclase Dron y pasa 
lo mismo con los métodos turnRadioOn() y turnRadioOff().

Para cumplir con el "Interface Segregation Principle" debemos refactorizar el código de forma que en vez de tener una única interfaz con 
demasiada responsabilidad tengamos tres interfaces con menor responsabilidad y que se adapten mejor a nuestro modelo y a la lógica de negocio.

Ahora la subclase Drone implementa la interfaz CameraSwitch y la subclase Car implementa la interfaz RadioSwitch. Ambas interfaces heredan 
de la interfaz común EngineSwitch.

"""