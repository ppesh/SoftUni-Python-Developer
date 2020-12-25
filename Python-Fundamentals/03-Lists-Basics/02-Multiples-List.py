# 02. Multiples List

factor = int(input())
count = int(input())

threshold = factor * count

my_list = list()
for i in range(factor, threshold + 1):
    if i % factor == 0:
        my_list.append(i)

print(my_list)

