from Crab import *


class Shrimp(Crab):

    def __init__(self, name, age, x, y, directionH):
        Crab.__init__(self, name, age,x, y, directionH)
        self.height = 3

    def __str__(self):
        return f"The shrimp {self.name} is {self.age} years old and has {self.food} food."

    def get_animal(self):
        if self.directionH == 0:
            return [["*", " ", "*", " ", " ", " ", " "],
               [" ", "*", "*", "*", "*", "*", "*"],
               [" ", " ", "*", " ", "*", " ", " "]]

        elif self.directionH == 1:
            return [[" ", " ", " ", " ", "*", " ", "*"],
                ["*", "*", "*", "*", "*", "*", " "],
                [" ", " ", "*", " ", "*", " ", " "]]
