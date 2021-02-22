# 01. Bombs
from collections import deque


def is_bomb_pouch_full(produced):
    return all([value >= 3 for value in produced.values()])


effects = deque(int(e) for e in input().split(", "))
casings = deque(int(c) for c in input().split(", "))


BOMBS_MATERIALS = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}

PRODUCED = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

while effects and casings and not is_bomb_pouch_full(PRODUCED):
    managed_to_produce = False
    for bomb_cost, bomb_name in BOMBS_MATERIALS.items():
        if bomb_cost == effects[0] + casings[-1]:
            PRODUCED[bomb_name] += 1
            effects.popleft()
            casings.pop()
            managed_to_produce = True
            break

    if not managed_to_produce:
        casings[-1] -= 5
        if casings[-1] < 0:
            casings.pop()


if not is_bomb_pouch_full(PRODUCED):
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print('Bene! You have successfully filled the bomb pouch!')

print(f"Bomb Effects: {', '.join(map(str, effects)) if effects else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, casings)) if casings else 'empty'}")

for bomb_type, num_of_bombs in sorted(PRODUCED.items()):
    print(f'{bomb_type}: {num_of_bombs}')