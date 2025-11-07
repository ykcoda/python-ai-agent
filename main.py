# OOP DEFINING CLASSES AND OBJECTS


class Robot:
    """This class implements a Robot"""

    population = 0  # a class attribute

    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year
        Robot.population += 1

    def setEnegy(self, energy):
        self.energy = energy


r1 = Robot("Robot1", 2025)
r2 = Robot("Robot2", 2050)
print(f"Robot name: {r1.name}")
r1.setEnegy(500)
print(r1.energy)

print(getattr(r1, "energy"))
print(r1.__dict__)

# print(r1.brand)
print(getattr(r1, "brand", "N/A"))


print(f"Robots alive: {Robot.population}")
