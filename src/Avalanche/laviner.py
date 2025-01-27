N, K, *A = map(int, open(0).read().split()); G = [[] for _ in range(N)]
for i in range(N-1): G[i+1].append(A[i]-1)
lo, hi = 0, 10**9
while lo < hi:
    s = [1]*N; w = 0; mi = (lo+hi)//2
    for u in range(N-1, -1, -1):
        if s[u] > mi: w += 1; s[u] = 0
        for v in G[u]: s[v] += s[u]
    if w <= K: hi = mi
    else: lo = mi+1
print(lo)