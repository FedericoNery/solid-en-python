import enum

class DrivingMode(enum.Enum):
    SPORT = 2
    COMFORT = 1

class EventHandler:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def changeDrivingMode(self, drivingMode):
        def sport(vehicle):
            vehicle.setPower(500)
            vehicle.setSuspensionHeight(10)

        def comfort(vehicle):
            vehicle.setPower(400)
            vehicle.setSuspensionHeight(20)

        def default(vehicle):
            vehicle.setPower(200);
            vehicle.setSuspensionHeight(30)

        switcher = {
            DrivingMode.SPORT: sport(self.vehicle),
            DrivingMode.COMFORT: comfort(self.vehicle),
        }

        func = switcher.get(drivingMode, lambda: default(self.vehicle))
        func()


class Vehicle:
    def __init__(self, power, suspensionHeight):
        self.power = power
        self.suspensionHeight = suspensionHeight

    def getPower(self):
        return self.power

    def setPower(self, power):
        self.power = power

    def getSuspensionHeight(self):
        return self.suspensionHeight

    def setSuspensionHeight(self, suspensionHeight):
        self.suspensionHeight = suspensionHeight
