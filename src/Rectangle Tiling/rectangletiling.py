from heapq import *
w, h, n, *a = map(int, open(0).read().split()); q = [(-w, h)]; z = 0
while q:
    w, h = heappop(q); ok = 0; w = -w
    for i in range(n-1, -1, -1):
        u = min(a[i], (h>>i)*(w>>i))
        if not u: continue
        a[i] -= u; z += u; ok = 1; r, m = divmod(u, w>>i)
        if h-(r+(m>0)<<i): heappush(q, (-w, h-(r+(m>0)<<i)))
        if m: heappush(q, (-w+(m<<i), 1<<i))
        if w-(w>>i<<i): heappush(q, (-w+(w>>i<<i), r<<i))
        break
    if not ok: print(-1); exit()
print(z)