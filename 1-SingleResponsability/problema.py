from typing import Final


class Vehicle:
    def __init__(self, max_fuel):
        self.maxFuel: Final = max_fuel
        self.remainingFuel = max_fuel


    def reFuel(self):
        self.remainingFuel = self.maxFuel

    def get_max_fuel(self):
        return self.maxFuel

    def get_remaining_fuel(self):
        return self.remainingFuel

