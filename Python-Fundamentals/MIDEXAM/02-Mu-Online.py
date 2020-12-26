# 02. Mu Online

initial_health = 100
bitcoins = 0
is_not_dead = False

current_room = 0
health = initial_health
dungeon_rooms = input().split("|")
# print(dungeon_rooms)

for i in range(len(dungeon_rooms)):
    current_room += 1
    room = dungeon_rooms[i].split()
    command = room[0]
    number = int(room[1])

    if command == "potion":
        if health + number > initial_health:
            print(f"You healed for {initial_health - health} hp.")
            health = initial_health
        else:
            health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        monster = command
        if health <= 0:
            is_not_dead = True
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {current_room}")
            break
        else:
            print(f"You slayed {monster}.")

if not is_not_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
