class RacingCar:
    def __init__(self, fuel):
        self.remainingFuel = fuel
        self.power = 0

    def accelerate(self):
        self.power += 1
        self.remainingFuel -= 1

class Driver:
    def __init__(self):
        self.racingCar = RacingCar(100)

    def increaseSpeed(self):
        self.racingCar.accelerate()
