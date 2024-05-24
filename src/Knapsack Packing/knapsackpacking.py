import sys; input = sys.stdin.readline
t = n = int(input()); k = sorted(int(input()) for _ in range(1<<n)); c = {}; a = []
if 0 not in k: print('impossible'), exit(0)
for i in k:
    if i not in c: c[i] = 0
    c[i] += 1
c[0] -= 1
for i in range(1, 1<<n):
    m = k[i]
    if c[m]:
        c[m] -= 1; a.append(m); z = 1; t -= 1; u = {}
        for j in range(i+1, 1<<n):
            if c[k[j]]:
                if k[j] not in u: u[k[j]] = 0
                u[k[j]] += 1; c[k[j]] -= 1
                if k[j]+m in c and c[k[j]+m]: c[k[j]+m] -= 1; z += 1
        if z != 1<<t: print('impossible'), exit(0)
        for i in u: c[i] += u[i]
print(*a)