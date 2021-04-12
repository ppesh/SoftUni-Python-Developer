# Problem 1 - 16 Dec. 2020
from collections import deque

# males = [int(m) for m in input().split()]
males = deque(int(m) for m in input().split())
females = deque(int(f) for f in input().split())

matches = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_male <= 0:
        males.pop()
    elif current_female <= 0:
        females.popleft()
    elif current_male % 25 == 0:
        males.pop()
        # males.pop()
    elif current_female % 25 == 0:
        females.popleft()
        # females.popleft()
    elif current_male == current_female:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {(', '.join(map(str, reversed(males))))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {(', '.join(map(str, females)))}")
else:
    print(f"Females left: none")