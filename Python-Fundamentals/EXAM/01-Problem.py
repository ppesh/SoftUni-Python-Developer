# 01. Problem

# Tests
"""
ILikeSharan
Replace a e
Make Upper
Check SHEREN
Sum 1 4
Cut 1 4
Finish

HappyNameDay
Replace p r
Make Lower
Cut 2 23
Sum -2 2
Finish
"""

def substitute(message_str, curr_char, repl_char):
    if curr_char in message_str:
        result = message_str.replace(curr_char, repl_char)
        print(result)
        return result
    else:
        return message_str


def cut(message_str, startIndex, endIndex):
    if startIndex > len(message_str) or startIndex < 0 or endIndex > len(message_str) or endIndex < 0:
        print("Invalid indices!")
        return message_str
    else:
        length = endIndex - startIndex
        result = message_str[:startIndex] + message_str[endIndex+1:]
        print(result)
        return result


def upplow(message_str, sub_command):
    if sub_command == "Upper":
        result = message_str.upper()
        print(result)
        return result
    elif sub_command == "Lower":
        result = message_str.lower()
        print(result)
        return result


def sumup(message_str, startIndex, endIndex):
    if startIndex > len(message_str) or startIndex < 0 or endIndex > len(message_str) or endIndex < 0:
        print("Invalid indices!")
        return message_str
    else:
        substr_sum = 0
        for i in range(startIndex, endIndex+1):
            substr_sum += ord(message_str[i])
        print(substr_sum)
        return substr_sum


string = input()

line = input()
while not line == "Finish":
    command = line.split()[0]
    if command == "Replace":
        current_char = line.split()[1]
        new_char = line.split()[2]
        string = substitute(string, current_char, new_char)
    elif command == "Cut":
        start_index = int(line.split()[1])
        end_index = int(line.split()[2])
        string = cut(string, start_index, end_index)
    elif command == "Make":
        upp_low = line.split()[1]
        string = upplow(string, upp_low)
    elif command == "Check":
        substring = line.split()[1]
        if substring in string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif command == "Sum":
        start_index = int(line.split()[1])
        end_index = int(line.split()[2])
        Sum = sumup(string, start_index, end_index)

    line = input()