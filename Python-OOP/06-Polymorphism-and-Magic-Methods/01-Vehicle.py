from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if distance * (self.fuel_consumption + 0.9) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if distance * (self.fuel_consumption + 1.6) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + 1.6)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


# Test Code
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

12.299999999999997
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
64.5
