from Fish import *

class Molly(Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        Fish.__init__(self, name, age, x, y, directionH, directionV)
        self.height = 3

    def __str__(self):
        return f"The molly {self.name} is {self.age} years old and has {self.food} food."

    def get_animal(self):
        if self.directionH == 0:
            return [[" ", "*", "*", "*", "*", " ", " ", "*"],
              ["*", "*", "*", "*", "*", "*", "*", "*"],
              [" ", "*", "*", "*", "*", " ", " ", "*"]]

        elif self.directionH == 1:
            return [["*", " ", " ", "*", "*", "*", "*", " "],
               ["*", "*", "*", "*", "*", "*", "*", "*"],
               ["*", " ", " ", "*", "*", "*", "*", " "]]
