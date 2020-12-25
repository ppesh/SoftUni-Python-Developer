# 04. Sum of Chars

n = int(input())
total_sum = 0
for i in range(0, n):
    letters = input()
    total_sum += sum(ord(i) for i in letters)       # The ord() function returns an integer representing the Unicode character.
print(f'The sum equals: {total_sum}')



