# 07. Decipher This!

deciphered_words = input().split()

for word in deciphered_words:
    first_decryption = []
    index_counter = 0
    for index in range(len(word)):
        if word[index].isdecimal():
            index_counter += 1
    first_decryption.append(word[:index_counter])
    list_to_str = "".join(first_decryption)
    right_char = chr(int(list_to_str))
    second_decryption = word[index_counter:]
    second_decryption_list = []
    for n in second_decryption[:]:
        second_decryption_list.append(n)
    second_decryption_list[0], second_decryption_list[-1] = second_decryption_list[-1], second_decryption_list[0]
    final_str = "".join(second_decryption_list)
    right_char += final_str
    print(right_char, end=" ")


