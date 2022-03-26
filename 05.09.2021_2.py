class Road:
    def __init__(self, lengh, width):
        self._length = lengh
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


road = Road(100, 5000)
print(road.calc_mass(), 'т')
