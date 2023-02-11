class Auto1:
    def __init__(self, car_brand, color, engine_capacity):
        self.car_brand = car_brand
        self.color = color
        self.engine_capacity = engine_capacity

    def drive_forvard(self):
        print("The car is moving forward.")

    def drive_back(self):
        print("The car is moving backward.")

class Auto2(Auto1):
    def __init__(self, car_brand, color, engine_capacity):
        Auto1.__init__(self, car_brand, color, engine_capacity)

    def drive_right(self):
        print("Car turns right.")

    def drive_left(self):
        print("Car turns left.")

car1 = Auto1('Mersedes', 'red', 2000)
print(car1.car_brand)
car1.drive_forvard()

car2 = Auto2('BMW', 'black', 1700)
car2.drive_left()
print(car2.color)