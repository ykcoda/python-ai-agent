# OOP DEFINING CLASSES AND OBJECTS


class Robot:
    """This class implements a Robot"""

    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year


r1 = Robot("Robot1", 2025)
print(f"Robot name: {r1.name}")
