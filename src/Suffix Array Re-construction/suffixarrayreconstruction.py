import sys; input = sys.stdin.readline
for _ in range(int(input())):
    l, s = map(int, input().split()); ok = 1; z = ['@']*l
    for _ in range(s):
        p, x = input().strip().split(); p = int(p)-1
        if not ok: continue
        x = x.split('*')
        for i in range(len(x[0])):
            if z[i+p] != '@' and z[i+p] != x[0][i]: ok = 0; break
            z[i+p] = x[0][i]
        if len(x) < 2 or not ok: continue
        for i in range(-1, -len(x[1])-1, -1):
            if z[i] != '@' and z[i] != x[1][i]: ok = 0; break
            z[i] = x[1][i]
    print(''.join(z) if ok and '@' not in z else 'IMPOSSIBLE')