# 03. Periodic Table

n = int(input())

chemical_elements = set()

for _ in range(n):
    chemical_compounds = input().split()
    for element in chemical_compounds:
        chemical_elements.add(element)

for element in chemical_elements:
    print(element)