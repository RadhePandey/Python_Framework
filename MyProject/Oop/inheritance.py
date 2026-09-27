class car():
    color = "White"

    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")

class HondaCar(car):
    def __init__(self,name):
        self.name = name

car1 = HondaCar("Honda City")
car1.stop()
car1.name()
# print(car1.name)
# print(car1.color)
# print(car1.start())
# print(car1.stop())