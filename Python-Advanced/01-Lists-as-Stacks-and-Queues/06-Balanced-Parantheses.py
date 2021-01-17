# 06. Balanced Parantheses

open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(input_str):
    stack = []
    for i in input_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                # return "Unbalanced"
                return "NO"
    if len(stack) == 0:
        # return "Balanced"
        return "YES"
    else:
        # return "Unbalanced"
        return "NO"


# Driver code
string = input()
print(check(string))