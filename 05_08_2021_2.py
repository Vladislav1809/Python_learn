# создаю функцию, которая считает сумму цифр числа
def sum_of_digits(x):
    summa = 0
    while x:
        summa += x % 10
        x //= 10
    return summa


# массив из условия задачи
mass_of_cubes = [x ** 3 for x in range(1, 1001, 2)]
# print(mass_of_cubes)

# финальные суммы, которые идут в ответ (пункт а и пункт б)
answer_summa_1 = 0
answer_summa_2 = 0
# основная программа
for number in mass_of_cubes:
    new_number = number + 17
    if sum_of_digits(number) % 7 == 0:
        answer_summa_1 += number
    if sum_of_digits(new_number) % 7 == 0:
        answer_summa_2 += new_number
print(answer_summa_1)
print(answer_summa_2)

