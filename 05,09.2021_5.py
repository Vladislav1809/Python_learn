class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()

