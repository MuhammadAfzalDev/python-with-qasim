# Basic Class and object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_details(self):
        return f"{self.brand} {self.model}"    
#Inheritance   
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
my_tesla = ElectricCar("Tesla", "Model S", "90Kw")
print(my_tesla.display_details())  # Output: Tesla Model S


class Student:
    
    def __init__(self, name, age, Fees):
        self.name = name
        self.age = age
        self.Fees = Fees
        print("Student Card created successfully")
s1 = Student("Muhammad Afzal", 27, 1000)
print(s1.name)
print(s1.age)
print(s1.Fees)



# my_car = Car("Honda", "Civic")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.display_details())

# Encapsulation

