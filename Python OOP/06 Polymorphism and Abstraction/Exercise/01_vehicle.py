from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    FUEL_COEFFICIENT = 0.9
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_consumed = (self.fuel_consumption + self.FUEL_COEFFICIENT) * distance
        if self.fuel_quantity > fuel_consumed:
            self.fuel_quantity -= fuel_consumed

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    FUEL_COEFFICIENT = 1.6
    FUEL_CAPACITY_COEFFICIENT = 0.95
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_consumed = (self.fuel_consumption + self.FUEL_COEFFICIENT) * distance
        if self.fuel_quantity > fuel_consumed:
            self.fuel_quantity -= fuel_consumed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_CAPACITY_COEFFICIENT


#Test Code
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
