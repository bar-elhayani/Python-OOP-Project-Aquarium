from Animal import *

class Crab(Animal):

    def __init__(self, name, age, x, y, directionH):
        Animal.__init__(self, name, age, x, y, directionH)
        self.width = 7

    def __str__(self):
        pass

    def get_animal(self):
        pass

    def move(self):
        if self.directionH == 0:
            self.x -= 1
        elif self.directionH == 1:
            self.x += 1
