s = [*input()]; a = 0
while True:
    b = a
    for i in range(len(s)-2):
        if s[i] == 'P' and s[i+2] == 'C': a += 1; s[i], s[i+2] = s[i+2], s[i]; break
    if a == b:
        for i in range(len(s)-2):
            if not (s[i] <= s[i+1] <= s[i+2]): a += 1; s[i:i+3] = sorted(s[i:i+3]); break
        if a == b: break
print(a)