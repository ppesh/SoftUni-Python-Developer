# 05. Palindrome Integers

def is_palindrome(list_of_number):
    for index in range(0, len(list_of_number)):
        reversed_number = list_of_number[index][::-1] 		# !!! [::-1] to reverse elemets (123 -> 321)
        if reversed_number == list_of_number[index]:
            print('True')
        else:
            print('False')


input_num = input().split(', ')
is_palindrome(input_num)
