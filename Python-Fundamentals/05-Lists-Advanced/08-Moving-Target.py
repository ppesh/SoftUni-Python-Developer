# *08. Moving Target

target_value = list(map(int, input().split()))
 
while True:
    instructions = input()
    if "End" in instructions:
        break
    command, index, value = instructions.split()
    index = int(index)
    value = int(value)
    if command == "Shoot":
        if 0 <= index < len(target_value):
            target_value[index] -= value
            if target_value[index] <= 0:
                target_value.pop(index)
    elif command == "Add":
        if 0 <= index >= len(target_value):
            print("Invalid placement!")
        else:
            target_value.insert(index, value)
    else:
        left_index = index - value
        right_index = index + value
        if left_index >= 0 and right_index < len(target_value):
            target_value = target_value[:left_index] + target_value[right_index + 1:]
        else:
            print("Strike missed!")
 
print("|".join(map(str, target_value)))


