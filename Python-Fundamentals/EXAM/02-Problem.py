# 02. Problem

# Tests
"""
3
##>|no|NO|!!!?<###
##>123|yes|YES|!!!<##
$$<111|noo|NOPE|<<>$$


5
aa>111|mqu|BAU|mqu<aa
()>111!aaa!AAA!^&*<()
o>088|abc|AAA|***<o
asd>asd|asd|ASD|asd<asd
*>088|zzzz|ZzZ|123<*
"""

import re

pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<\1"
n = int(input())

for i in range(n):
    line = input()

    if re.match(pattern, line):
        data = line.split('|')
        data = ''.join(data)
        data = data.split('>')[1]
        data = data.split('<')[0]
        print(f"Password: {data}")
    else:
        print("Try another password!")
