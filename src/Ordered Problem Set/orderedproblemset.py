n = int(input())
a = [int(input()) for _ in range(n)]
c = []
for k in range(2, n+1):
    if n%k == 0:
        ok = 1; P = [[] for _ in range(k)]
        for p in range(1, n+1): P[(k*p+n-1)//n-1].append(a[p-1])
        for i in range(k):
            for j in range(i+1, k):
                if max(P[i]) >= min(P[j]): ok = 0; break
            if not ok: break
        if ok: c.append(k)
if not c: print(-1)
else:
    for i in c: print(i)