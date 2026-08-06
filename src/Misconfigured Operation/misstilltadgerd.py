from array import *; import sys; input = sys.stdin.readline
N, M = map(int, input().split())
s, t = map(int, input().split())
E = []; INF = 10**9; s -= 1; t -= 1
for _ in range(M): a, b, w = input().split(); a = int(a)-1; b = int(b)-1; m = w[0]=='-'; k = int(w.split('^')[1]); E.append((a, (b+m*N)%(2*N), k)); E.append((a+N, (b+m*N+N)%(2*N), k))
D = array('i', [INF]*2*N); D[s] = 0
F = array('i', [-INF]*2*N); F[s] = 0
for _ in range(2*N-1):
    for a, b, w in E:
        if D[a] != INF and D[b] > D[a]+w: D[b] = D[a]+w
        if F[a] != -INF and F[b] < F[a]+w: F[b] = F[a]+w
z = D[t]; y = F[t+N]
for _ in range(2*N-1):
    for a, b, w in E:
        if D[a] != INF and D[b] > D[a]+w: D[b] = D[a]+w
        if F[a] != -INF and F[b] < F[a]+w: F[b] = F[a]+w
    if y != F[t+N]: print('-infinity'); exit()
    elif z != D[t]: print('epsilon'); exit()
if F[t+N] != -INF: print(f'-2^{F[t+N]}')
elif D[t] != INF: print(f'2^{D[t]}')
else: print('unreachable')