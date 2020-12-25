# 03. Next Version

version = input().split(".")
new = int("".join(version))
new_version = int(new + 1)
print(".".join(str(new_version)))

"""
old_version = "".join(map(str, input().split(".")))
new_version = ".".join(str(int(old_version) + 1))
print(new_version)
"""


