# 01. Count Chars in a String

test_str = input().split()

res = {}

# using dict.get() to get count
# of each element in string

for keys in "".join(test_str):
    res[keys] = res.get(keys, 0) + 1

# printing result
# key = character, value = occurrences 
for key, value in res.items():
    print(f"{key} -> {value}")