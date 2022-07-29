import sys


numb_line, new_line = sys.argv[1:]


with open('bakery.csv', 'r+', encoding='utf-8') as fin:
    file = open('bake.txt', 'w+', encoding='utf-8')
    flag = False
    for ind, line in enumerate(fin, 1):
        if ind == numb_line:
            file.write(f"{new_line}\n")
            flag = True
        else:
            file.write(line)
    if not flag:
        exit('error')

    file.seek(0)

    fin.truncate(0)
    for line in file:
        fin.write(line)
    file.close()


