N = int(input()); P = [*map(float, input().split())]; H = {}; B = [-1]*N
for bm in range(1, 1<<N):
    if bin(bm).count('1') == 1:
        for i in range(N):
            if bm&(1<<i): z = [0]*N; z[i] = 1; H[bm*N+i] = z
        continue
    for i in range(N):
        if bm&(1<<i) == 0: continue
        h = []; H[bm*N+i] = [0]*N
        for j in range(N):
            if bm&(1<<j) == 0 or i == j: continue
            k = (i+1)%N; bm2 = bm^(1<<j)
            while bm2&(1<<k) == 0: k += 1; k %= N
            h.append((H[bm2*N+k][i], -j, bm2, k))
        _, _, bm2, k = max(h); B[i] = [P[i]*x for x in H[bm2*N+k]] # B[i] = P(win if i hits given initial state bm)
    for i in range(N):
        if bm&(1<<i) == 0: continue
        for j in range(N):
            q = 1; p = 0
            for k in range(i, i+N): # simulate whole round
                k %= N
                if bm&(1<<k): p += q*B[k][j]; q *= 1-P[k]
            H[bm*N+i][j] = p/(1-q)
print(*H[(N<<N)-N])