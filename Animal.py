from Exceptions import *
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, x, y, directionH):
        if not isinstance(name, str):
            raise InvalidInputException
        if name == '':
            raise InvalidInputException
        if not isinstance(age, int):
            raise InvalidInputException
        if age <= 0 or age >= 120:
            raise InvalidInputException
        if not isinstance(x, int):
            raise InvalidInputException
        if x <= 0:
            raise InvalidInputException
        if not isinstance(y, int):
            raise InvalidInputException
        if y <= 0:
            raise InvalidInputException
        if not isinstance(directionH, int):
            raise InvalidInputException
        if directionH != 0 and directionH != 1:
            raise InvalidInputException
        self.name = name
        self.age = age
        self.food = 10
        self.directionH = directionH
        self.x = x
        self.y = y

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_animal(self):
        pass

    def __repr__(self):
        empty = ''
        for char in self.get_animal():
            empty += ' '.join(char[:-1]) + ' ' + char[-1] + '\n'
        return empty

    def get_position(self):
        return self.x, self.y

    def get_directionH(self):
        return self.directionH

    def get_size(self):
        return self.width, self.height

    def dec_food(self):
        self.food -= 1

    def add_food(self, amount):
        self.food += amount

    def inc_age(self):
        self.age += 1

    @abstractmethod
    def move(self):
        pass

    def set_directionH(self, directionH):
        self.directionH = directionH

    def starvation(self):
        if self.food == 0:
            print(f"{self.name} died at the age of {self.age} years because it ran out of food.")
            return True
        else:
            return False

    def die(self):
        if self.age >= 120:
            print(f"{self.name} died in a good health.")
            return True
        else:
            return False

