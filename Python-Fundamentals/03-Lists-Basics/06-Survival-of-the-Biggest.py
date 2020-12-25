# 06. Survival of the Biggest

list_of_int = [int(el) for el in input().split()]
num = int(input())

for i in range(0, num):
    list_of_int.remove(min(list_of_int))

print(list_of_int)

