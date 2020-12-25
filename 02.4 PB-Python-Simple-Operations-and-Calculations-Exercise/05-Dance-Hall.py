# 05.Dance Hall

length = float(input())     # in m
width = float(input())      # in m
side_w = float(input())     # in m

area_room = length * width
# print(area_room)
area_w = side_w * side_w
# print(area_w)
area_bench = area_room / 10
# print(area_bench)

dancer = 40 / 10000
dancer_space = 7000 / 10000       # in sqm

free_space = area_room - area_w - area_bench
num_dancers = free_space / (dancer + dancer_space)

print(int(num_dancers))



