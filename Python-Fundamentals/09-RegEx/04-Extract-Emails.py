# 04. Extract Emails

import re

data = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+"
# pattern = r"(^|(?=\s))_(?P<name>[A-Za-z0-9]+)($|(?=\s))"

result = re.finditer(pattern, data)

for el in result:
    print(el.group())

# (^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@                   -   user
# [a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+($|(?=\s))     -   host