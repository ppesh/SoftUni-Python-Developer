# 03. Problem

# Tests
"""
New follower: george
Like: george: 5
Comment: george
New follower: george
New follower: john
Comment: george
Comment: john
Comment: peter
Log out


Like: A: 3
Comment: A
New follower: B 
Blocked: A
Comment: B 
Like: C: 5
Like: D: 5
Log out 
"""


line = input()

followers = {}

while not line == "Log out":
    command = line.split(": ")[0]
    username = line.split(": ")[1]

    if command == "New follower":
        if username not in followers:
            # followers[username] = {'likes': int(0), 'comments': int(0)}
            followers[username] = 0
    elif command == "Like":
        count = int(line.split(": ")[2])
        if username not in followers:
            followers[username] = count
        else:
            followers[username] += count
    elif command == "Comment":
        if username not in followers:
            followers[username] = 1
        else:
            followers[username] += 1
    elif command == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

    line = input()

print(f"{len(followers)} followers")

sorted_followers = sorted(followers.items(), key=lambda x: (-x[1], x[0]))
for username, value in sorted_followers:
    print(f"{username}: {value}")