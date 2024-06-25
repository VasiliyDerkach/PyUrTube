class Vehicle:
    def __init__(self):
        self.vehicle_type = None

class Car:
    def __init__(self):
        self.price = 1000000
        self.horse_power = 90
    def horse_powers(self):
        return self.horse_power

class Nissan(Car, Vehicle):
    def __init__(self,vehicle_type,price,horse_power):
        super().__init__()
        self.vehicle_type= vehicle_type
        self.price=  price
        self.horse_power= horse_power
    def horse_powers(self):
        return f' мощность: {self.horse_power}'
    def __str__(self):
        return f'{self.vehicle_type}, {self.price}, {self.horse_powers()}'

if __name__=='__main__':
    Auto= Nissan('Karina',50,25)
    print(Auto)
