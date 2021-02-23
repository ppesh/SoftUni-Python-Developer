# 03. Numbers Search

def numbers_searching(*args):
    min_num = min(args)
    max_num = max(args)
    result = find_missing_value(args, min_num, max_num)
    result.append(find_duplicates(args))
    return result


def find_duplicates(nums):
    return sorted(list(set([n for n in nums if nums.count(n) > 1])))


def find_missing_value(nums, min_num, max_num):
    start, end = min_num, max_num
    return sorted(set(range(start, end + 1)).difference(nums))


# Input
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))