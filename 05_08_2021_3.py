word = 'процент'
finish_of_word_1 = 'а'
finish_of_word_2 = 'ов'
for x in range(1, 101):
    ost = x % 10
    if ost == 1 and not(11 <= x <= 14):
        print(x, word)
    elif 2 <= ost <= 4 and not(11 <= x <= 14):
        print(x, word + finish_of_word_1)
    elif 5 <= ost <= 9 or ost == 0 or (11 <= x <= 14):
        print(x, word + finish_of_word_2)

