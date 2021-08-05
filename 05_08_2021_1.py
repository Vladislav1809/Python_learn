# входные данные
duration = int(input())

# переменные для удобства
second_in_minute = 60
second_in_our = second_in_minute * 60
second_in_day = second_in_our * 24

# словарь, содержащий информацию о днях, часах, минутах и секундах
inf_about_duration = {}.fromkeys(['дн', 'час', 'мин', 'сек'], 0)

# заполнение словаря
if duration >= second_in_day:
    inf_about_duration['дн'] = duration // second_in_day
    duration -= inf_about_duration['дн'] * second_in_day
if duration >= second_in_our:
    inf_about_duration['час'] = duration // second_in_our
    duration -= inf_about_duration['час'] * second_in_our
if duration >= second_in_minute:
    inf_about_duration['мин'] = duration // second_in_minute
    duration -= inf_about_duration['мин'] * second_in_minute
inf_about_duration['сек'] = duration

# печать словаря
for key, val in inf_about_duration.items():
    if val != 0:
        print(val, key, end=' ')

