# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Subclass 4
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()
