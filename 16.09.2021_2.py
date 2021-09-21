from abc import ABC, abstractmethod


class Clother(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clother):

    @property
    def calculate(self):
        return round((self.data / 6.5) + 0.5)


class Suit(Clother):

    @property
    def calculate(self):
        return round((2 * self.data) + 0.3)


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)
