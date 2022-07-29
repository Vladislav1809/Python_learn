import sys


cost = sys.argv[1]


with open('bakery.csv', 'a', encoding='utf-8') as bakery:
    bakery.write(cost + '\n')
