# 01. Invert Values

input_string = input().split()

my_list = list()
for i in range(0, len(input_string)):
    # print(-1 * int(input_string[i]), sep=',', end=' ')
    new_element = -1 * int(input_string[i])
    my_list.append(new_element)

print(my_list)
