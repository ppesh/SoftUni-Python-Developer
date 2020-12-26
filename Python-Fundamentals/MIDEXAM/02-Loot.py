# 02. Loot

def check_item_exist(loot_list, item):
    return True if item in loot_list else False


loot = input().split("|")

command = input()
while not command == "Yohoho!":
    command_type = command.split()[0]

    if command_type == "Loot":
        found_items = command.split()
        found_items.remove(command_type)
        # print(found_items)
        for i in range(0, len(found_items)):
            if not check_item_exist(loot, found_items[i]):
                loot.insert(0, found_items[i])
        # print(loot)
    elif command_type == "Drop":
        index = int(command.split()[1])
        if 0 <= index < len(loot):
            item_to_be_moved = loot[index]
            loot.remove(item_to_be_moved)
            loot.append(item_to_be_moved)
        # print(loot)
    elif command_type == "Steal":
        stolen_items = []
        count = int(command.split()[1])
        if count > len(loot):
            for i in range(0, len(loot)):
                stolen_items.append(loot[-1])
                loot.pop()
        else:
            for i in range(0, count):
                stolen_items.append(loot[-1])
                loot.pop()
        stolen_items.reverse()
        print(', '.join(stolen_items))

    command = input()

treasure_gain = 0
for el in loot:
    treasure_gain += len(el)
if len(loot) > 0:
    average_treasure_gain = treasure_gain / len(loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")