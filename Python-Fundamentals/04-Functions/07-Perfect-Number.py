# 07. Perfect Number

def perfect_number(n):
    s = 0
    for x in range(1, n):
        if n % x == 0:
            s += x
    return s == n


num = int(input())

if perfect_number(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
