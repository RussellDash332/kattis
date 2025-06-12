V = int(input()); P = [[*map(int, input().split())] for _ in range(V)]; G = [((P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2+(P[i][2]-P[j][2])**2)**.5 if i!=j else 1e9 for i in range(V) for j in range(V)]; C = {1<<i:i for i in range(V)}; D = [-1]*(1<<V)*V*2
def dp(n, bm, op):
    if D[z:=bm*V*2+n*2+(1<<n&op>0)] > -1: return D[z]
    if not bm: return 0 if z%2 and op%2 else G[n*V]
    bm2 = bm; x = 1e9
    while bm2:
        nxt = bm2&-bm2
        if z%2 and op&nxt: x = min(x, dp(C[nxt], bm^nxt, op^nxt^(1<<n)))
        x = min(x, G[n*V+C[nxt]]+dp(C[nxt], bm^nxt, op)); bm2 ^= nxt
    D[z] = x; return x
print(dp(0, (1<<V)-2, (1<<V)-1))