# 07. Water Overflow

capacity = 255
tank = 0
n = int(input())
for i in range(0, n):
    water_quantities = int(input())
    tank += water_quantities
    if tank > capacity:
        print("Insufficient capacity!")
        tank -= water_quantities
        continue

print(tank)




