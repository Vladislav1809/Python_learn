"""
from random import random, randint, shuffle


input_massive_1 = [round(random() * 100, 2) for x in range(10)]
input_massive_2 = [randint(1, 101) for y in range(10)]
input_massive = input_massive_1 + input_massive_2
shuffle(input_massive)
print(input_massive)
"""

# input data
cost_massive = [12.82, 84, 67.28, 5.09, 59.44, 5, 52.54, 16, 28.15, 32,
                95, 59, 81, 39, 51.58, 29.02, 85, 56.97, 41, 29.89]

# item A
print('item A')
for cost in cost_massive:
    print(f'{int(cost)} руб {round((cost - int(cost)) * 100):02d} коп,',  end=' ')
print()
print()

# item B
print('item B')
cost_massive.sort()
for cost in cost_massive:
    print(f'{int(cost)} руб {round((cost - int(cost)) * 100):02d} коп,',  end=' ')
    print(f'Index of the element = {cost_massive.index(cost)}, element = {cost}')
print()

# item C
print('item C')

print(*sorted(cost_massive, reverse=True))
print()

# item D
print('item D')
# РАЗНЫЕ ВАРИАНТЫ РЕАЛИЗАЦИИ
# ВАРИАНТ 1 (самый короткий вариант ("некрасивый" вывод))
print(sorted(cost_massive[-5:]))

# ВАРИАНТ 2 (та же идея вывода, но более "красивым" образом)
print(', '.join(map(str, sorted(cost_massive[-5:]))))

