# 01. Activation Key

def cut(raw_pass, i, length):
    result = raw_pass[:i] + raw_pass[i+length:]
    # print(result)
    return result


def substitute(raw_input, sub_command, str_to_be_replaced):
    if sub_command == "Upper":
        repl = str_to_be_replaced.upper()
    elif sub_command == "Lower":
        repl = str_to_be_replaced.lower()
    result = raw_input.replace(str_to_be_replaced, repl)
    print(result)
    return result


raw_input = input()
line = input()

while not line == "Generate":
    command = line.split(">>>")[0]
    if command == "Contains":
        substring = line.split(">>>")[1]
        if substring in raw_input:
            print(f"{raw_input} contains {substring}")
        else:
            print(f"Substring not found!")
    elif command == "Flip":
        substring = line.split(">>>")[1]
        start_index = int(line.split(">>>")[2])
        end_index = int(line.split(">>>")[3])
        subsubstring = raw_input[start_index:end_index]
        raw_input = substitute(raw_input, substring, subsubstring)
    elif command == "Slice":
        start_index = int(line.split(">>>")[1])
        end_index = int(line.split(">>>")[2])
        raw_input = cut(raw_input, start_index, end_index-start_index)
        print(raw_input)
    line = input()

print(f"Your activation key is: {raw_input}")