from typing import Final

# Refuel no es responsabilidad de la clase 'Vehicle'

class Vehicle:
    def __init__(self, max_fuel):
        self.maxFuel: Final = max_fuel
        self.remainingFuel = max_fuel

    def get_max_fuel(self):
        return self.maxFuel

    def get_remaining_fuel(self):
        return self.remainingFuel

    def set_remaining_fuel(self, remainingFuel):
        self.remainingFuel = remainingFuel

class FuelPump:
    @staticmethod
    def reFuel(vehicle):
        remainingFuel = vehicle.get_remaining_fuel()
        additionalFuel = vehicle.get_max_fuel() - remainingFuel
        vehicle.setRemainingFuel(remainingFuel + additionalFuel)
