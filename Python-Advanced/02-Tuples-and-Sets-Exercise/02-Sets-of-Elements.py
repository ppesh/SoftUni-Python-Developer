# 02. Sets of Elements

n, m = tuple([int(x) for x in input().split()])

set_n = set()
set_m = set()

for _ in range(n):
	set_n.add(input())
	
for _ in range(m):
	set_m.add(input())
	
set_intersection = set_n & set_m

for element in set_intersection:
	print(element)