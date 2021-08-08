def is_int_in_elem(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


# input data
input_massive = ['в', '5', 'часов', '17', 'минут', 'температура',
                 'воздуха', 'была', '+5', 'градусов']

x = len(input_massive)
ind = 0
while ind < x:
    if is_int_in_elem(input_massive[ind]):
        if '+' in input_massive[ind] or '-' in input_massive[ind]:
            input_massive[ind] = input_massive[ind].zfill(3)
        else:
            input_massive[ind] = input_massive[ind].zfill(2)

        input_massive.insert(ind, '"')
        input_massive.insert(ind+2, '"')
        x += 2
        ind += 2
    else:
        ind += 1

# сборка строки
final_str = ''
x = len(input_massive)
i = 0
while i < x:
    if input_massive[i] == '"':
        final_str += ' ' + input_massive[i] + input_massive[i + 1] + input_massive[i + 2]
        i += 2
    else:
        final_str += ' ' + input_massive[i]
    i += 1
print(final_str)

