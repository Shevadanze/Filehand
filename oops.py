# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__engine_status = False   # Encapsulation (private attribute)

    def start_engine(self):
        if not self.__engine_status:
            self.__engine_status = True
            print(f"{self.year} {self.make} {self.model}'s engine started.")
        else:
            print(f"{self.year} {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.__engine_status:
            self.__engine_status = False
            print(f"{self.year} {self.make} {self.model}'s engine stopped.")
        else:
            print(f"{self.year} {self.make} {self.model}'s engine is already off.")

    # Polymorphic method
    def move(self):
        print(f"{self.year} {self.make} {self.model} is moving...")

# Subclass 1
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    # Override move method (Polymorphism)
    def move(self):
        print(f"The car {self.make} {self.model} drives smoothly on the road.")

# Subclass 2
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, cc):
        super().__init__(make, model, year)
        self.cc = cc

    # Override move method (Polymorphism)
    def move(self):
        print(f"The motorcycle {self.make} {self.model} zooms at high speed!")

# Create objects
car1 = Car("Toyota", "Corolla", 2022, 4)
bike1 = Motorcycle("Yamaha", "R1", 2021, 1000)

# Demonstrate functionality
car1.start_engine()
car1.move()
car1.stop_engine()

print("---")

bike1.start_engine()
bike1.move()
bike1.stop_engine()
