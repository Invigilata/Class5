class Car:
    price = 1000000

    def horse_powers(self):
        return 120

class Nissan(Car):
    def __init__(self):
        self.price = 1500000

    def horse_powers(self):
        return 200

class Kia(Car):
    def __init__(self):
        self.price = 1200000

    def horse_powers(self):
        return 150

# Пример использования классов
car = Car()
print(car.price)
print(car.horse_powers())

nissan = Nissan()
print(nissan.price)
print(nissan.horse_powers())

kia = Kia()
print(kia.price)
print(kia.horse_powers())
