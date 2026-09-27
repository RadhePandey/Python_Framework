class Car:
    wheels = 4
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model} has {self.wheels} wheels.")

car1 = Car("Toyota", "Fortuner")


car1.display_info()






# car2 = Car("Honda", "City")
# car2.display_info()