from Animal import *
from Exceptions import *
class Fish(Animal):

    def __init__(self, name, age, x, y, directionH, directionV):
        if directionV != 0 and directionV != 1:
            raise InvalidInputException
        Animal.__init__(self, name, age, x, y, directionH)
        self.width = 8
        self.directionV = directionV

    def get_directionV(self):
        return self.directionV

    def set_directionV(self, directionV):
        self.directionV = directionV

    def __str__(self):
        pass

    def get_animal(self):
        pass

    def move(self):
        if self.directionH == 0:
           if self.directionV == 0:
                self.y += 1
                self.x -= 1
           elif self.directionV == 1:
               self.y -= 1
               self.x -= 1
        elif self.directionH == 1:
            if self.directionV == 0:
                self.x += 1
                self.y += 1
            elif self.directionV == 1:
                self.x += 1
                self.y -= 1
