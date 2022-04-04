class Cell:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        return 'The sum of cells is ' + str(self.data + other.data)

    def __sub__(self, other):
        return self.data - other.data if self.data - other.data > 0 \
            else 'Вычитание не возможно'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.data * other.data)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.data / other.data))

    def order(self, numb_rows):
        return '\n'.join(['*' * numb_rows for _ in range(self.data // numb_rows)]) + '\n' \
               + '*' * (self.data % numb_rows)


cell_1 = Cell(10)
cell_2 = Cell(5)

# print(cell_1 - cell_2)
# print(cell_1 + cell_2)
# print(cell_1 / cell_2)
# print(cell_1 * cell_2)
# print(cell_1.order(4))
