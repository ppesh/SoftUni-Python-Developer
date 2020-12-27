# 01. Secret Chat

def insert(message_str, index_str):
    result = message_str[:index_str] + ' ' + message_str[index_str:]
    print(result)
    return result
 
 
def reverse(message_str, sub_str):
    if sub_str in message_str:
        result = message_str.replace(sub_str, "", 1) + sub_str[::-1]
        print(result)
        return result
    else:
        print("error")
        return message_str
 
 
def substitute(message_str, sub_str, repl):
    if sub_str in message_str:
        result = message_str.replace(sub_str, repl)
        print(result)
        return result
    else:
        return message_str
 
 
message = input()
strings = input()
 
while not strings == "Reveal":
    command = strings.split(":|:")[0]
    if command == "InsertSpace":
        index = int(strings.split(":|:")[1])
        message = insert(message, index)
    elif command == "Reverse":
        substring = strings.split(":|:")[1]
        message = reverse(message, substring)
    elif command == "ChangeAll":
        substring = strings.split(":|:")[1]
        replacement = strings.split(":|:")[2]
        message = substitute(message, substring, replacement)
 
    strings = input()
 
print(f"You have a new text message: {message}")