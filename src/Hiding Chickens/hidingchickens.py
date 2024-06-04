r = complex(*map(float, input().split())); N = int(input()); P = [complex(*map(float, input().split())) for _ in range(N)]; D = [-1]*(1<<N); C = {(1<<i):i for i in range(N)}; G = [abs(r-P[i]) for i in range(N)]

# Weighted MCM - dp with bitmask
def dp(bm):
    if abs(D[bm]+1) > 1e-7: return D[bm]
    # root -> C[nxt] -> root
    nxt = bm&-bm; a = 2*G[C[nxt]]+dp(bm^nxt); bm2 = bm^nxt
    # root -> C[nxt] -> C[nxt2] -> root
    while bm2: nxt2 = bm2&-bm2; bm2 ^= nxt2; a = min(a, G[C[nxt]]+abs(P[C[nxt]]-P[C[nxt2]])+G[C[nxt2]]+dp(bm^nxt^nxt2))
    D[bm] = a; return a

# we don't need to return back to root after hiding the last chicken
# since there exists a path (root -> C[i]) or (C[i] -> root) for all i, we can just remove the largest of such
D[0] = 0; print(dp((1<<N)-1)-max(G))