with open('nginx_logs.txt') as fin:
    string = fin.readline()
    users_dict = {}
    while string != '':
        users = string[:string.find(' ') - 1]
        users_dict.setdefault(users, 0)
        users_dict[users] += 1
        string = fin.readline()
print(*max(users_dict.items(), key=lambda k_v: k_v[1]))
