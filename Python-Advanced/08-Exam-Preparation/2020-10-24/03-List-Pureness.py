# 03. List Pureness

from collections import deque


def best_list_pureness(nums, k):
    nums_deque = deque(nums)
    highest_pureness = calculate_pureness(nums)
    rotations_count = 0
    for r in range(k+1):
        current_pureness = calculate_pureness(nums_deque)
        if highest_pureness < current_pureness:
            highest_pureness = current_pureness
            rotations_count = r
        nums_deque.rotate()
    return f"Best pureness {highest_pureness} after {rotations_count} rotations"


def calculate_pureness(nums):
    pureness = 0
    for (index, num) in enumerate(nums):
        pureness += index * num
    return pureness


# Test Code 1
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

# Test Code 2
test2 = ([7, 9, 2, 5, 3, 4], 3)
result2 = best_list_pureness(*test2)
print(result2)

# Test Code 3
test3 = ([1, 2, 3, 4, 5], 10)
result3 = best_list_pureness(*test3)
print(result3)