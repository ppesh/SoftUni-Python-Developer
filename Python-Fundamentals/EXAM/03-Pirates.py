# 03. P!rates

cities = {}

command = input()
while not command == "Sail":
    city = command.split("||")[0]
    population = int(command.split("||")[1])
    gold = int(command.split("||")[2])

    if city not in cities:
        cities[city] = []
        cities[city].append(population)
        cities[city].append(gold)
    else:
        cities[city][0] += population
        cities[city][1] += gold

    command = input()

# print(cities)

events = input()

while not events == "End":
    command = events.split("=>")[0]
    town = events.split("=>")[1]

    if command == "Plunder":
        people = int(events.split("=>")[2])
        plunder = int(events.split("=>")[3])

        cities[town][0] -= people
        cities[town][1] -= plunder
        print(f"{town} plundered! {plunder} gold stolen, {people} citizens killed.")

        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        plunder = int(events.split("=>")[2])

        if plunder < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += plunder
            print(f"{plunder} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    events = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    ordered_cities = dict(sorted(cities.items(), key=lambda x: (-x[1][1], x[0])))
    for key, value in ordered_cities.items():
        people = value[0]
        gold = value[1]
        print(f"{key} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")