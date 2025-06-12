import sys; input = sys.stdin.readline
N, K = map(int, input().split()); A = {}; Z = 0
if K == 1: print(1); exit()
for i, v in enumerate(map(int, input().split())):
    if v not in A: A[v] = []
    A[v].append(i)
for p in A.values():
    lo, hi = 0, 1
    while abs(lo-hi)>1e-7:
        mi = (lo+hi)/2; l = v = 0; m = 1e18; ok = 0
        for r in range(len(p)):
            while p[r]-p[l]+1 >= K: m = min(m, l-mi*p[l]); l += 1
            v = max(v, (r-l+1)/K)
            if v > mi or m+mi-1 < r-mi*p[r]: ok = 1; break
        if ok: lo = mi
        else: hi = mi
    Z = max(Z, mi)
print(Z)