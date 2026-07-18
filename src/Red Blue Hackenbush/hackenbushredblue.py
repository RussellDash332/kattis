N, M = map(int, input().split()); N += 1; G = [[] for _ in range(N)]; B = [-1]*2**M; H = [(0, -1) for _ in B]; E = []
for i in range(M): a, b, c = input().split(); G[a:=max(int(a), 0)] += [(b:=max(int(b), 0), i)]; G[b] += [(a, i)]; E += [(a, b, 2*(c<'R')-1)]
def conn(bm):
    if ~B[bm]: return B[bm]
    V = 1; Q = [z:=0]
    for u in Q:
        for v, i in G[u]:
            if bm&(1<<i) and V&(1<<v)<1: V |= 1<<v; Q += [v]
    for i in range(M):
        if bm&(1<<i):
            a, b, _ = E[i]
            if V&(1<<a)>0<V&(1<<b): z |= 1<<i
    B[bm] = z
    return B[bm]
def simp(p, q, r, s): # /hackenbushsimplicity
    m = max(q, s)
    if p<<(m-q) > r<<(m-s): p, q, r, s = r, s, p, q
    def f(x): return p<<(x-q) if x>q else ~(~p>>(q-x)), r<<(x-s) if x>s else (~-r>>(s-x))+1
    for lo in range(0, m+2):
        a, b = f(lo)
        if b-a > 1: break
    if a*b < 0: return (0, 0)
    n = [b-1, a+1][b>0]
    while lo and n%2<1: n //= 2; lo -= 1
    return (n, lo)
def find(bm):
    if ~H[bm][1]: return H[bm]
    b = (-25, 0); r = (25, 0)
    for i in range(M):
        if bm&(1<<i)<1: continue
        x, y = find(conn(bm^(1<<i)))
        if E[i][2]>0:
            p, q = b; m = max(q, y)
            if p<<(m-q) < x<<(m-y): b = (x, y)
        else:
            p, q = r; m = max(q, y)
            if p<<(m-q) > x<<(m-y): r = (x, y)
    H[bm] = simp(*b, *r); return H[bm]
p, q = find(conn(2**M-1)); print(f'{p}/2^{q}' if q else p)