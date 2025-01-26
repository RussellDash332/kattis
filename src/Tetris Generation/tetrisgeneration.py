import sys; input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip(); z = 0
    for i in range(min(7, len(s))):
        ok = 1
        t = {s[j] for j in range(i)}
        if len(t) != i: ok = 0; continue
        for j in range(i, len(s), 7):
            t = {s[j+k] for k in range(min(7, len(s)-j))}
            if len(t) != min(7, len(s)-j): ok = 0; break
        z = max(z, ok)
    print(z)