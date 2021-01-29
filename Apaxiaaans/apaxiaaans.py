name = input()
result = name[0]
for k in name[1:]:
    if result[-1] != k:
        result += k
print(result)