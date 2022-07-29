with open('nginx_logs.txt') as fin:
    output_massive = []
    string = fin.readline()
    while string != '':
        fin_string = string.split()
        output_massive.append((
            fin_string[0],
            fin_string[5].replace('"', ''),
            fin_string[6]
        ))
        string = fin.readline()
print(output_massive)
