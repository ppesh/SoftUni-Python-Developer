# 04. Fashion Boutique

clothes = [int(x) for x in input().split()]
capacity = int(input())

sum_clothes = 0
count_racks = 0

while clothes:
    if sum_clothes + clothes[-1] <= capacity:
        sum_clothes += clothes[-1]
        clothes.pop()
    else:
        sum_clothes = 0
        count_racks += 1
        sum_clothes += clothes[-1]
        clothes.pop()

if sum_clothes > 0:
    count_racks += 1

print(count_racks)