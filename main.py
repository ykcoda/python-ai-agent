# MAGIC OBJECTS


class Robot:
    """This class implements a Robot"""

    population = 0  # a class attribute

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        Robot.population += 1

    def setEnegy(self, energy):
        self.energy = energy

    def __str__(self):
        my_str = f"My name is {self.name} and i am priced ${self.price}"
        return my_str

    def __add__(self, other):
        return self.price + other.price


r1 = Robot("r1", 34)
r2 = Robot("r2", 250)

print(r1 + r2)
