# 03. Elevator

import math

num_people = int(input())
c = int(input())                     # capacity

courses = math.ceil(num_people / c)
print(courses)


