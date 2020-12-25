# 04. Odd and Even Sum

def sum_odd_even(num):
    length = len(number)
    odd_sum = 0
    even_sum = 0
    for i in range(0, length):
        if int(num[i]) % 2 == 0:
            even_sum += int(num[i])
        else:
            odd_sum += int(num[i])
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


number = input()
sum_odd_even(number)
