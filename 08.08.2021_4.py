# input data
input_massive = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for elem in input_massive:
    print(f'Привет, {elem.split(" ")[-1].capitalize()}!')

