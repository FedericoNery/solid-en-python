from abc import ABC, abstractmethod

# Cuando necesitemos añadir otro modo(e.g.ECONOMY)  deberemos cambiar la clase 'EventHandler' y la enumeración 'DrivingMode'.

class DrivingMode (ABC):
    @abstractmethod
    def getPower(self):
        pass

    @abstractmethod
    def getSuspensionHeight(self):
        pass


class Comfort(DrivingMode):
    POWER = 400;
    SUSPENSION_HEIGHT = 20;

    def getPower(self):
        return Comfort.POWER

    def getSuspensionHeight(self):
        return Comfort.SUSPENSION_HEIGHT

class Sport(DrivingMode):
    POWER = 500
    SUSPENSION_HEIGHT = 10

    def getPower(self):
        return Sport.POWER

    def getSuspensionHeight(self):
        return Sport.SUSPENSION_HEIGHT

class EventHandler:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def changeDrivingMode(self, drivingMode):
        self.vehicle.setPower(drivingMode.getPower())
        self.vehicle.setSuspensionHeight(drivingMode.getSuspensionHeight());
        #Ahora, cuando necesitemos añadir otro modo (e.g. ECONOMY) sólo hay que crear la clase 'Economy'.
