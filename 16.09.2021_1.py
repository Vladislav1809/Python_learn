class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.data])

    def __add__(self, other):
        answer = ''
        if len(self.data) == len(other.data):
            for line_1, line_2 in zip(self.data, other.data):
                if len(line_1) != len(line_2):
                    return 'Some error'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, sum_line)) + '\n'
        else:
            return 'Some error'

        return answer


m_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_2 = Matrix([[2, 3], [4, 5], [5, 6]])
print(m_1)
print()
print(m_2)
print()
print(m_1 + m_2)
