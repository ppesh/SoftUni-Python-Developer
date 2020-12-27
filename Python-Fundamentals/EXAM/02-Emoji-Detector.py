# 02. Emoji Detector

import re

string = input()

regex = r"([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)"
matches = re.findall(regex, string)

cool_threshold = 1
for char in string:
    if char.isdigit():
        cool_threshold *= int(char)

cool_emojis = []
for emoji in matches:
    coolness = 0
    for char in emoji[1]:
        coolness += ord(char)
    if coolness > cool_threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {cool_threshold}')
if len(matches) > 0:
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for emoji in cool_emojis:
        print(''.join(emoji))