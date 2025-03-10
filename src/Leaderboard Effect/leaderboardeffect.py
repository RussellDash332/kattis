from array import *
n, T = map(int, input().split())
P = array('f'); R = array('b'); C = array('b')
B = array('i', [1<<i for i in range(n)])
for i in range(n): r, c, p = map(float, input().split()); R.append(int(r)); C.append(int(c)); P.append(p)
D = [array('f', [0]*(1<<n)) for _ in range(T+1)]
E = [array('d', [0]*n) for _ in range(T+1)]
U = [[] for _ in range(1<<n)]
for i in range(1<<n):
    for j in range(n):
        if i&B[j] == 0: U[i].append(j)
D[0][0] = 10**8
for i in range(T+1):
    E[i] = [E[i][j]+E[i-1][j] for j in range(n)]
    for k in range(1<<n):
        if D[i][k] == 0: continue
        u = v = 0
        for j in U[k]:
            u += E[i][j]; v += 1
        for j in U[k]:
            x = E[i][j]/u if u else 1/v
            if i+R[j]+C[j] < T+1: p = D[i][k]*P[j]*x; D[i+R[j]+C[j]][k|B[j]] += p; E[i+R[j]+C[j]][j] += p
            if i+R[j] < T+1: D[i+R[j]][k|B[j]] += D[i][k]*(1-P[j])*x
print(*(x/10**8 for x in E[-1]))