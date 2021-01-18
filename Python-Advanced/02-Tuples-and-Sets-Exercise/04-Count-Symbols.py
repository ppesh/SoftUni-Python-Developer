# 04. Count Symbols

text = input()

chars_dict = {}

for ch in text:
	if ch not in chars_dict:
		chars_dict[ch] = 0
	chars_dict[ch] += 1
	
for (key, value) in sorted(chars_dict.items()):
	print(f"{key}: {value} time/s")