n, t, *a = map(int, open(0).read().split())
for i in range((n+1)//2):
    if t < 1: break
    if a[2*i]:
        c = 1; t -= 1
        for j in range(2*i, n):
            a[j] += 1; c -= 1
            if c < 1:
                if a[j] == 1: break
                else: c = a[j]; a[j] = 0
    a[2*i] = t%2
    if 2*i+1 < n: t = t//2; a[2*i+1] += t
print(*a)