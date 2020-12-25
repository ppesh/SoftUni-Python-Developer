# 07. Maximum Multiple

d = int(input())           # divisor
b = int(input())           # bound

n = b
while n > 0:
    if n % d == 0:
        print(n)
        break
    else:
        n -= 1



