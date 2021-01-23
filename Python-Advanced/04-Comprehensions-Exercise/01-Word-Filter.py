# 01. Word Filter

elements = input().split()
filtered = [x for x in elements if len(x) % 2 == 0]
# 1. variant:
# [print(x) for x in filtered]	
# 2. variant:
print('\n'.join(filtered))


