class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25
    def __init__(self,fuel: float, horse_power: int) -> None:
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: float) -> None:
        fuel_consumed = self.fuel_consumption * kilometers
        if self.fuel >= fuel_consumed:
            self.fuel -= fuel_consumed
