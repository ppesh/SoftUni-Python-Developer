# 01. Which Are In?
"""
substrings = input().split(", ")
words = input().split(", ")


result = [subst for subst in substrings for word in words if subst in word]

print(sorted(set(result), key=result.index))

# Set {} - A set is a collection which is unordered and not indexed.
# set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements
# set() is unordered collection

"""
"""
result = []

for word in words:
    for subst in substrings:
        if subst in word and subst not in result:
            result.append(subst)

print(result)
"""


first_string = input().split(", ")
second_string = input()

words = list(filter(lambda x: x in second_string, first_string))

print(words)

