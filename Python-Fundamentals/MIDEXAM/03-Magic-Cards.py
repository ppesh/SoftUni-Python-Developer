# 03. Magic Cards

def check_card_exist(all_cards_list, card):
    return True if card in all_cards_list else False


all_cards = input().split(":")

deck = []

command = input()
while not command == "Ready":
    command_type = command.split()[0]

    if command_type == "Add":
        card_name = command.split()[1]
        if check_card_exist(all_cards, card_name):
            deck.append(card_name)
        else:
            print("Card not found.")
    elif command_type == "Insert":
        card_name = command.split()[1]
        index = int(command.split()[2])
        if check_card_exist(all_cards, card_name) and 0 <= index < len(deck):
            deck.insert(index, card_name)
        else:
            print("Error!")
    elif command_type == "Remove":
        card_name = command.split()[1]
        if check_card_exist(deck, card_name):
            deck.remove(card_name)
        else:
            print("Card not found.")
    elif command_type == "Swap":
        card_name_1 = command.split()[1]
        card_name_2 = command.split()[2]
        index_1 = deck.index(card_name_1)
        index_2 = deck.index(card_name_2)
        deck[index_1] = card_name_2
        deck[index_2] = card_name_1
    elif command_type == "Shuffle":
        deck.reverse()

    command = input()

print(' '.join(deck))