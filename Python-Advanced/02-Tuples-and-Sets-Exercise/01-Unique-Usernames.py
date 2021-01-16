# 01. Unique Usernames

num_usernames = int(input())

unique_usernames = set()

for _ in range(num_usernames):
	username = input()
	unique_usernames.add(username)
	
for username in unique_usernames:
	print(username)