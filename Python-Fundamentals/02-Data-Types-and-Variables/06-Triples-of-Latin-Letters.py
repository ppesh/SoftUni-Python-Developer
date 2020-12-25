# 06. Triples of Latin Letters

n = int(input())
a_small_letter_ascii = ord('a')

for first_char in range(0, n):
    for second_char in range(0, n):
        for third_char in range(0, n):
            print(f"{chr(97 + first_char)}{chr(97 + second_char)}{chr(97 + third_char)}")       # 97 = a





