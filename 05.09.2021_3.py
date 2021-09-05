class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname} {self.position}"

    def get_total_income(self):
        return self._income_wage + self._income_bonus


wage_bonus = {'wage': 100000, 'bonus': 1000000}
person = Position('Maxim', 'Maximov', 'beginner', wage_bonus)
print(person.get_full_name())
print(person.get_total_income())
