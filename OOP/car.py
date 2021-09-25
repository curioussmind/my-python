# class car
class Car:
    
    def __init__(self, color, mileage):
        self.color = color # isntamce attributes
        self.mileage = mileage # instance attributes
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles."

    def drive(self, number):
        total = number + self.mileage
        return total

# car_blue = Car("blue", 20000)
# print(car_blue)

# car_red = Car("red", 30000)
# print(car_red)

green_car = Car("green", 0)
green_car.drive(100)
print(green_car)
print(green_car.mileage)

