from Molly import *
from Scalar import *
from Ocypode import *
from Shrimp import *
from Exceptions import *


class Aquarium():
    def __init__(self, aqua_width, aqua_height):
        if not isinstance(aqua_width, int):
            raise InvalidInputException
        if aqua_width < 40:
            raise TooSmallAquariumSize
        if not isinstance(aqua_height, int):
            raise InvalidInputException
        if aqua_height < 25:
            raise TooSmallAquariumSize

        self.aqua_width = aqua_width
        self.aqua_height = aqua_height
        self.step = 0
        self.animals = []
        self.board = []
        for y in range(0, aqua_height):
            inner_list = []
            if y == 2:
                for x in range(0, aqua_width):
                    if x == 0:
                        inner_list.append('|')
                    elif x == aqua_width - 1:
                        inner_list.append('|')
                    elif 0 < x < (aqua_width - 1):
                        inner_list.append('~')
                self.board.append(inner_list)

            elif y == aqua_height -1:
                for x in range(0, aqua_width):
                    if x == 0:
                        inner_list.append('\\')
                    elif x == aqua_width -1:
                        inner_list.append('/')
                    elif 0 < x < (aqua_width -1):
                        inner_list.append('_')
                self.board.append(inner_list)

            elif 0 <= y < 2 or 2 < y < aqua_height -1:
                for x in range(0, aqua_width):
                    if x == 0:
                        inner_list.append('|')
                    elif x == aqua_width -1:
                        inner_list.append('|')
                    elif 0 < x < (aqua_width -1):
                        inner_list.append(' ')
                self.board.append(inner_list)

    def __str__(self):
        strs = ''
        for ani in self.animals:
            x = ani.__str__()
            strs += x + '\n'
        return f"The aquarium, sized {self.aqua_height}/{self.aqua_width} and currently in step {self.step}, contains the following animals:\n{strs}"

    def __repr__(self):
        empty = ''
        for row in self.board:
            empty += ' '.join(row[:-1]) + ' ' + row[-1] + '\n'
        return empty

    def feed_all(self):
        for ani in self.animals:
            ani.add_food(10)

    def __insert_animal_to_board(self, animal):
        ani = animal.get_animal()
        x = animal.x
        y = animal.y
        for i in range(len(ani)):
            for j in range(len(ani[i])):
                if 0 <= y + i < len(self.board) and 0 <= x + j < len(self.board[0]):
                    if ani[i][j] == "*":
                        self.board[y + i][x + j] = "*"

    def __delete_animal_from_board(self, animal):
        ani = animal.get_animal()
        x = animal.x
        y = animal.y

        for i in range(len(ani)):
            for j in range(len(ani[i])):
                if 0 <= y + i < len(self.board) and 0 <= x + j < len(self.board[0]):
                    if ani[i][j] == "*":
                        self.board[y + i][x + j] = " "

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if x <= 0:
            x = 1
        if y <= 2:
            y = 3
        if animaltype == 'scalar':
            new_ani = Scalar(name, age, x, y, directionH, directionV)
            if y > self.aqua_height - 10:
                new_ani.y = self.aqua_height - 10
            elif y < 3:
                new_ani.y = 3
            if x < 1:
                new_ani.x = 1
            elif x >= self.aqua_width -9:
                new_ani.x = self.aqua_width - 9
        elif animaltype == 'molly':
            new_ani = Molly(name, age, x, y, directionH, directionV)
            if y > self.aqua_height - 8:
                new_ani.y = self.aqua_height - 8
            elif y < 3:
                new_ani.y = 3
            if x < 1:
                new_ani.x = 1
            elif x >= self.aqua_width -9:
                new_ani.x = self.aqua_width -9
        elif animaltype == 'ocypode':
            new_ani = Ocypode(name, age,x, y, directionH)
            if y != self.aqua_height - 5:
                new_ani.y = self.aqua_height - 5
            if x < 1:
                new_ani.x = 1
            elif x >= self.aqua_width -8:
                new_ani.x = self.aqua_width -8
        elif animaltype == 'shrimp':
            new_ani = Shrimp(name, age, x, y, directionH)
            if y != self.aqua_height - 4:
                new_ani.y = self.aqua_height - 4
            if x < 1:
                new_ani.x = 1
            elif x >= self.aqua_width -8:
                new_ani.x = self.aqua_width -8
        else:
            raise InvalidAnimalType(animaltype)

        new_ani_upper_y, new_ani_lower_y = new_ani.y, new_ani.y + (new_ani.height -1)
        new_ani_left_x, new_ani_right_x = new_ani.x, new_ani.x + (new_ani.width -1)
        for ani in self.animals:
            ani_x, ani_y = ani.get_position()
            ani_x_right, ani_y_lower = ani_x + (ani.width - 1), ani_y + (ani.height -1)
            if (new_ani_upper_y <= ani_y <= new_ani_lower_y) or (new_ani_upper_y <= ani_y_lower <= new_ani_lower_y):
                if (new_ani_left_x <= ani_x <= new_ani_right_x) or (new_ani_left_x <= ani_x_right <= new_ani_right_x):
                    raise NotAvailablePlace

        self.__insert_animal_to_board(new_ani)
        self.animals.append(new_ani)

    def __kill_animal(self, animal):
        if animal.starvation():
            self.__delete_animal_from_board(animal)
            self.animals.remove(animal)
        elif animal.die():
            self.__delete_animal_from_board(animal)
            self.animals.remove(animal)

    def next_step(self):
        self.step += 1

        for ani in self.animals:
            self.__kill_animal(ani)

        for ani in self.animals:
            self.__delete_animal_from_board(ani)

        nesty_crab = [ani for ani in self.animals if isinstance(ani, (Shrimp, Ocypode))]
        for crabi in nesty_crab:
            for crabus in nesty_crab:
                if (crabi.x + crabi.width == crabus.x or crabi.x + crabi.width == crabus.x - 1) and (crabi.get_directionH() != crabus.get_directionH()) and (crabus.get_directionH() == 0):
                    if crabi.get_directionH() == 0:
                        crabi.set_directionH(1)
                    elif crabi.get_directionH() == 1:
                        crabi.set_directionH(0)
                    if crabus.get_directionH() == 0:
                        crabus.set_directionH(1)
                    elif crabus.get_directionH() == 1:
                        crabus.set_directionH(0)

        for ani in self.animals:
            if ani.x == 1:
                ani.set_directionH(1)
            elif ani.x == self.aqua_width - ani.width - 1:
                ani.set_directionH(0)

        for ani in self.animals:
            if type(ani) is Scalar or type(ani) is Molly:
                if ani.y == 3:
                    ani.set_directionV(0)
                elif ani.y == self.aqua_height - ani.height - 5:
                    ani.set_directionV(1)

        for ani in self.animals:
            ani.move()

        if self.step % 10 == 0:
            for ani in self.animals:
                ani.dec_food()
                ani.inc_age()

        for ani in self.animals:
            self.__insert_animal_to_board(ani)

    def several_steps(self, steps):
        for ste in range(steps):
            self.next_step()
