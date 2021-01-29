import re
name = input()
print("".join(re.findall(r"[A-Z]",name)))