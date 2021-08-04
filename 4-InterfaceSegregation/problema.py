from abc import ABC, abstractmethod

class Switches(ABC):
    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def turnRadioOn(self):
        pass

    @abstractmethod
    def turnRadioOff(self):
        pass

    @abstractmethod
    def turnCameraOn(self):
        pass

    @abstractmethod
    def turnCameraOff(self):
        pass

class Car(Switches):

    def __init__(self):
        self._radioOn = None

    def startEngine(self):
        pass

    def turnRadioOn(self):
        self._radioOn = True

    def turnRadioOff(self):
        self._radioOn = False

    def turnCameraOn(self):
        pass

    def turnCameraOff(self):
        pass

class Drone (Switches):

    def __init__(self):
        self._cameraOn = None

    def startEngine(self):
        pass

    def turnCameraOn(self):
        self._cameraOn = True

    def turnCameraOff(self):
        self._cameraOn = False

    def turnRadioOn(self):
        pass

    def turnRadioOff(self):
        pass
