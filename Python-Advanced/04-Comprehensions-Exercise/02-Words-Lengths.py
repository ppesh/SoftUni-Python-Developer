# 02. Words Lengths

# 1. variant with list:
elements = input().split(", ")
result = [f"{x} -> {len(x)}" for x in elements]
print(", ".join(result))

# 2. variant with dictionary:
elements = {x: len(x) for x in input().split(", ")}
result = [f"{key} -> {value}" for key, value in elements.items()]
print(", ".join(result))


