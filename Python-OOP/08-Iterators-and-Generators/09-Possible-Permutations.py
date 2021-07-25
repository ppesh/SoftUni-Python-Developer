from itertools import permutations


def possible_permutations(sequence):
    for per in permutations(sequence):
        yield list(per)


# Test Code
[print(n) for n in possible_permutations([1, 2, 3])]