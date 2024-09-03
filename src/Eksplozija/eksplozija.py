def check():
    if len(z) < len(t): return 0
    for i in range(len(t)):
        if t[i] != z[i-len(t)]: return 0
    return 1
s, t = input(), input(); z = []
for i in s:
    z.append(i)
    if check():
        for _ in range(len(t)): z.pop()
print(''.join(z) or 'FRULA')