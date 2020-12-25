# 01. Smallest of Three Numbers

def find_smallest(num1, num2, num3):
    if num1 < num2:
        if num1 < num3:
            print(num1)
        else:
            print(num3)
    elif num2 < num1:
        if num2 < num3:
            print(num2)
        else:
            print(num3)
    else:
        print(num3)


input_num1 = int(input())
input_num2 = int(input())
input_num3 = int(input())

find_smallest(input_num1, input_num2, input_num3)