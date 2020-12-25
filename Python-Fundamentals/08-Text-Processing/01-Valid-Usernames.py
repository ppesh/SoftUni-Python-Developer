# 01. Valid Usernames

user_name = input().split(", ")
count = 0

for el in user_name:
    if 3 < len(el) < 16:
        for i in range(0, len(el)):
            if el[i].isalpha() or el[i].isnumeric() or el[i] == "-" or el[i] == "_":
                count += 1
        if count == len(el):
            print(el)
            count = 0
        else:
            count = 0