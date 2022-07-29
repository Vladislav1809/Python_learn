from itertools import zip_longest
import sys
import json

# for number 5
if __name__ != "__main__":
    users_file, hobby_file, inform_file, text_file = sys.argv[1:]

if __name__ == "__main__":
    users_file, hobby_file, inform_file, text_file = ("users.csv", "hobby.csv",
                                                      "inf_about_users.json", "users_hobby.txt")


def users_list_creator(file):
    inf = []
    string = file.readline()
    while string != '':
        inf.append(string.strip())
        string = file.readline()
    return inf


def hobby_list_creator(file):
    inf = []
    string = file.readline()
    while string != '':
        inf.append(string.strip().split(','))
        string = file.readline()
    return inf


with open(users_file, encoding='utf-8') as users:
    with open(hobby_file, encoding='utf-8') as hobby:
        with open(inform_file, 'w', encoding='utf-8') as information_about_users:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for _ in hobby)
            if num_lines_hobby > num_lines_users:
                exit(1)
            users.seek(0)
            hobby.seek(0)
            inf_about_users = {name: hobby for name, hobby in
                               zip_longest(users_list_creator(users), hobby_list_creator(hobby))}
            json.dump(inf_about_users, information_about_users, ensure_ascii=False)  # for number 3

# for number 4-5
with open(text_file, "a", encoding='utf-8') as fin:
    for user, hobby in inf_about_users.items():
        if hobby is not None:
            fin.write(f"{user}: {', '.join(hobby)} \n")
        else:
            fin.write(f"{user}: {hobby}")
