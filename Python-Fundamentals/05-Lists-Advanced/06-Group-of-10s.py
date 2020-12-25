# 06. Group of 10's

list_of_num = input().split(", ")
group_boundary = 10
factor = 1

while list_of_num:
    group = [el for el in list_of_num if int(el) <= group_boundary * factor]
    print(f"Group of {group_boundary * factor}'s: [{', '.join(group)}]")
    for i in range(len(group)):
        list_of_num.remove(group[i])
    factor += 1




