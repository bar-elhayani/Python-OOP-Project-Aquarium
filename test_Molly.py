from unittest import TestCase
from Molly import *


class TestMolly(TestCase):
    def setUp(self):
        self.molly = Molly(name="Molly1", age=2, x=5, y=10, directionH=0, directionV=0)


    def test_molly_creation(self):
        self.assertEqual(self.molly.name, "Molly1")
        self.assertEqual(self.molly.age, 2)
        self.assertEqual(self.molly.x, 5)
        self.assertEqual(self.molly.y, 10)
        self.assertEqual(self.molly.directionH, 0)
        self.assertEqual(self.molly.directionV, 0)
        self.assertEqual(self.molly.height, 3)

    def test_molly_str_representation(self):
        expected_str = "The molly Molly1 is 2 years old and has 10 food."
        self.assertEqual(str(self.molly), expected_str)

    def test_molly_get_animal(self):
        expected_animal = [
            [" ", "*", "*", "*", "*", " ", " ", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*"],
            [" ", "*", "*", "*", "*", " ", " ", "*"]
        ]
        self.assertEqual(self.molly.get_animal(), expected_animal)

    def test_molly_movement(self):
        initial_x = self.molly.x
        self.molly.move()
        self.assertEqual(self.molly.x, initial_x - 1)

    def test_molly_food_handling(self):
        initial_food = self.molly.food
        self.molly.dec_food()
        self.assertEqual(self.molly.food, initial_food - 1)

        initial_food = self.molly.food
        self.molly.add_food(5)
        self.assertEqual(self.molly.food, initial_food + 5)

    def test_molly_age_incrementation(self):
        initial_age = self.molly.age
        self.molly.inc_age()
        self.assertEqual(self.molly.age, initial_age + 1)

