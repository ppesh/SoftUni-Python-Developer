# 02. A Miner Task

resources = {}
elements = []

command = input()

while not command == "stop":
    elements.append(command)
    command = input()

for i in range(0, len(elements), 2):
    key = elements[i]                       # resource
    value = int(elements[i + 1])            # quantity

    if key in resources:
        resources[key] += value
    else:
        resources[key] = value

for key, value in resources.items():
    print(f"{key} -> {value}")