# 05. SoftUni Parking

n = int(input())

parking_val = {}

for i in range(0, n):
    command = input()
    command_type = command.split()[0]
    username = command.split()[1]

    if command_type == "register":
        # print(1)
        # username = command.split()[1]
        plate_num = command.split()[2]
        if username not in parking_val:
            parking_val[username] = plate_num
            print(f"{username} registered {plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_num}")
    elif command_type == "unregister":
        # print(2)
        # username = command.split()[1]
        if username not in parking_val:
            print(f"ERROR: user {username} not found")
        else:
            parking_val.pop(username)
            print(f"{username} unregistered successfully")


for username, plate_num in parking_val.items():
    print(f"{username} => {plate_num}")