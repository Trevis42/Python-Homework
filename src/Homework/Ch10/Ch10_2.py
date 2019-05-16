class Car:

    def __init__(self, make, model):
        self.__setModel(model)
        self.__setMake(make)
        self.__speed = 0

    def __setModel(self, model):
        self.__year_model = model
    def __setMake(self, make):
        self.__make = make

    def getModel(self):
        return self.__year_model
    def getMake(self):
        return self.__make

    def setSpeed(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5

def main():
    c1 = Car("Toyota", "Corolla")

    print("Accelerating!!")
    for s in range(1, 6):
        c1.accelerate();
        print("Current Speed:", c1.get_speed())
    print("\nBraking!!")
    for b in range(1, 6):
        c1.brake();
        print("Current Speed:", c1.get_speed())


main()
