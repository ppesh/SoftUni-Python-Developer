# 03. Inventory

def check_item_exist(journal_list, item_searched):
    return True if item_searched in journal_list else False


journal = input().split(", ")

command = input()
while not command == "Craft!":
    command_type = command.split(" - ")[0]
    item = command.split(" - ")[1]

    if command_type == "Collect":
        if not check_item_exist(journal, item):
            journal.append(item)
    elif command_type == "Drop":
        if check_item_exist(journal, item):
            journal.remove(item)
    elif command_type == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if check_item_exist(journal, old_item):
            current_index = journal.index(old_item)
            journal.insert(current_index+1, new_item)
    elif command_type == "Renew":
        if check_item_exist(journal, item):
            journal.remove(item)
            journal.append(item)

    command = input()

print(', '.join(journal))