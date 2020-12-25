# 02. Add and Subtract

def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(num12, num3):
    result = num12 - num3
    return result


def add_and_subtract(num1, num2, num3):
    result1 = sum_numbers(num1, num2)
    result2 = subtract(result1, num3)
    print(result2)


input_num1 = int(input())
input_num2 = int(input())
input_num3 = int(input())

add_and_subtract(input_num1, input_num2, input_num3)
