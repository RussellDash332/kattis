from functools import *
M = 10**9+7
for tc in range(int(input())):
    N = int(input()); D = [*map(int, str(N))]
    @cache
    def dp(d, t, s, bm):
        if d == len(D): return {bm or 1:1}
        z = {}
        for i in range((D[d]+1, 10)[t]):
            for k, v in dp(d+1, t|(i<D[d]), s or i, bm|(1<<i) if s or i else bm).items():
                if k not in z: z[k] = 0
                z[k] += v
        return z
    C = [0]*1024; Z = [*C]; Z[0] = 1
    for k, v in dp(0, 0, 0, 0).items(): C[k] = v
    C[1] -= 1 # remove 0
    for x in range(1, 1024):
        if C[x]<1: continue
        z = [*Z]
        for y in range(1024):
            if x&y<1: z[x|y] += Z[y]*C[x]
        Z = z
    print(f'Case {tc+1}: {(sum(Z)-Z[0])%M}')