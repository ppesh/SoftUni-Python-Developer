# 01. World Tour

def insert(stops_str, index_str, repl):
    if index_str in range(len(stops_str)):
        return stops_str[:index] + repl + stops_str[index:]
    return stops_str


def remove(stops_str, start, end):
    if start in range(len(stops_str)) and end in range(len(stops_str)):
        return stops_str[:start] + stops_str[end + 1:]
    return stops_str


def substitute(stops_str, sub_str, repl):
    if sub_str in stops_str:
        result = stops_str.replace(sub_str, repl)
    return result


stops = input()
line = input()

while not line == "Travel":
    command = line.split(":")[0]
    if command == "Add Stop":
        index = int(line.split(":")[1])
        string = line.split(":")[2]
        stops = insert(stops, index, string)
        print(stops)
    elif command == "Remove Stop":
        start_index = int(line.split(":")[1])
        end_index = int(line.split(":")[2])
        stops = remove(stops, start_index, end_index)
        print(stops)
    elif command == "Switch":
        old_string = line.split(":")[1]
        new_string = line.split(":")[2]
        stops = substitute(stops, old_string, new_string)
        print(stops)

    line = input()

print(f"Ready for world tour! Planned stops: {stops}")