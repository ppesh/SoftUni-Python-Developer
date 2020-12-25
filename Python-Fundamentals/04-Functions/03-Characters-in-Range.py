# 03. Characters in Range

def char_in_range(char1, char2):
    start = ord(char1)
    end = ord(char2)

    for i in range(start+1, end):
        print(chr(i), end=' ')


input_char1 = input()
input_char2 = input()

char_in_range(input_char1, input_char2)
