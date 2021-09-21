import random


class Loto:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._NUMBERS = 90
        MAX_NUM = 90
        self._numb_in_card = random.sample(range(1, MAX_NUM + 1), self._NUMBERS)

    def _get_numb(self):
        return self._numb_in_card.pop()

    def game(self):
        hard_level = int(input('Введите уровень сложности (1-Легко, 2-Средне, 3-Сложно): '))
        for i in range(self._NUMBERS):
            print(self._player, self._computer)
            number = self._get_numb()
            print(f'Новый бочонок {number}, осталось {len(self._numb_in_card)}')
            get_choise = input('Хотите зачеркнуть? y/n: \n')
            if get_choise == 'y':
                if not self._player.try_numb(number):
                    print('Игрок проиграл')
                    print('Такого числа нет')
                    break
            elif self._player.has_num(number):
                print('Игрок проиграл')
                print('Такое число есть')
                break
            if hard_level < 3:
                if hard_level == 1:
                    if random.random() < 0.1:
                        print('Компьютер ошибся')
                        print('Вы победили!')
                        break
                if hard_level == 2:
                    if random.random() < 0.03:
                        print('Компьютер ошибся')
                        print('Вы победили!')
                        break
            elif self._computer.has_num(number):
                self._computer.try_numb(number)


class Card:

    def __init__(self, type_of_player):
        self.type_of_player = type_of_player
        self._card = [[],
                      [],
                      []]
        self._MAX_NUMB = 90
        self._MAX_COUNT_OF_NUMB_IN_CARD = 15
        self._numbers_stroked = 0
        WHITESPACE = 4
        NEED_NUMB = 5
        self._numbers = random.sample(range(1, self._MAX_NUMB + 1), self._MAX_COUNT_OF_NUMB_IN_CARD)

        for line in self._card:
            for _ in range(WHITESPACE):
                line.append(' ')
            for _ in range(NEED_NUMB):
                line.append(self._numbers.pop())

        def check_sort(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._MAX_NUMB)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort)

    def has_num(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_numb(self, number):
        for index, line in enumerate(self._card):
            for num_ind, numb_in_card in enumerate(line):
                if number == numb_in_card:
                    self._card[index][num_ind] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._MAX_COUNT_OF_NUMB_IN_CARD:
                        raise Exception(f'{self.type_of_player} победил')
                    return True
        return False

    def __str__(self):
        MAX_LENGTH = 3
        header = f'\n{self.type_of_player}:\n--------------------------'
        body = '\n'
        for line in self._card:
            for i in line:
                body += str(i).ljust(MAX_LENGTH)
            body += '\n'
        return header + body


human = Card('Игрок')
computer = Card('Компьютер')

game = Loto(human, computer)
game.game()
