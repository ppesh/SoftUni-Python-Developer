# 05. Can't Sleep? Count Sheep

integer = int(input())
result = ""
count_sheep = 0
for i in range(0, integer):
    count_sheep += 1
    result += str(count_sheep) + " sheep..."
print(result)


