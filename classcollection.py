class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car:
    def __init__(self):
        self.price = 1000000
        self.horse_power = 90
    def horse_powers(self):
        return self.horse_power

class Nissan(Car, Vehicle):
    def __init__(self,vehicle_type,price,horse_power):
        super().__init__()