# 02. Destination Mapper

import re

string = input()

regex = r"(=|\/)([A-Z]{1}[A-Za-z]{2,})(\1)"
matches = re.findall(regex, string)

destinations = []
travel_points = 0
for destination in matches:
    destinations.append(destination[1])
    travel_points += len(destination[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")