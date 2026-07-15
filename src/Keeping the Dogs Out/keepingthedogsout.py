# /rectangletiling
from heapq import *
def f(w, h, a):
    n = len(a); q = [(-w, h)]; z = 0
    while q:
        w, h = heappop(q); ok = 0; w = -w
        for i in range(n-1, -1, -1):
            u = min(a[i], (h>>i)*(w>>i))
            if not u: continue
            a[i] -= u; z += u; ok = 1; r, m = divmod(u, w>>i)
            if h-(r+(m>0)<<i): heappush(q, (-w, h-(r+(m>0)<<i)))
            if m: heappush(q, (-w+(m<<i), 1<<i))
            if r and w-(w>>i<<i): heappush(q, (-w+(w>>i<<i), r<<i))
            break
        if not ok: return 0
    return 1
N, *A = map(int, open(0).read().split())
S = sum(A[i]<<(2*i) for i in range(N+1))
if S < 1: print(0, 0)<exit()
for a in range(1, int(S**.5)+2):
    if S%a == 0: b = S//a; f(a, b, [*A]) and print(a, b)<exit()
print('impossible')