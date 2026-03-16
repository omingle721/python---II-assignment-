

# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")


# Subclass Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road")


# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Creating objects
car1 = Car()
bike1 = Bicycle()

# Demonstrating polymorphism
car1.move()
bike1.move()