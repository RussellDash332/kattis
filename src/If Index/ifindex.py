D = 0; V = []
for i in input().replace('if', '.'):
    if i == '{': D += 1
    elif i == '}': D -= 1
    else: V.append(D)
V.sort(); print(V[(len(V)-1)//2] if V else -1)