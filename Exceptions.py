class InvalidInputException(Exception):
    pass


class NotAvailablePlace(Exception):
    pass


class TooSmallAquariumSize(Exception):
    pass


class InvalidAnimalType(Exception):
    def __init__(self,animal):
        self.animal = animal
    def __str__(self):
        return f"Error: {str(self.animal)} is an invalid animal type. The valid animal types are: molly, scalar, ocypode, shrimp."
