# 03. Find Occurances of Word in Sentence

import re
data = input()
searched = input()

pattern = f"\\b{searched}\\b"

result = re.findall(pattern, data, re.IGNORECASE)

print(len(result))