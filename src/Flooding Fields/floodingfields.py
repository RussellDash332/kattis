import sys; input = sys.stdin.readline; from collections import deque; from array import *
def add(u, v, c): AL[u].append(len(EL)); EL.append(v*K+c); AL[v].append(len(EL)); EL.append(u*K)
N, K, H = map(int, input().split()); T = array('b'); Z = ((0, -1), (-1, 0), (1, 0), (0, 1), (0, 0)); V = 2*N*N*(H+1)+2; source, sink = V-2, V-1; EL, AL = array('i'), [[] for _ in range(V)]; mf = 0; p = array('i', [-1]*V); K += 1; H += 1
for _ in range(N): T.extend(map(int, input().split()))
for _ in range(K-1): r, c = map(int, input().split()); add(source, 2*(r*N+c)*H, 1) # cows
F = array('b', [-1]+[int(input()) for _ in range(H-1)])
for i in range(N*N):
    for t in range(H): add(x:=2*i*H+2*t, x+1, 1) # vertex cap
for i in range(N*N):
    for t in range(H-1):
        if T[i] > F[t]:
            r, c = divmod(i, N)
            for dr, dc in Z:
                if N>r+dr>-1<c+dc<N and T[(r+dr)*N+c+dc] > F[t+1]: add(2*i*H+2*t+1, 2*((r+dr)*N+c+dc)*H+2*(t+1), 1) # move to next timeframe
    if T[i] > F[-1]: add(2*i*H+2*H-1, sink, 1) # survived
while True:
    d = array('b', [0]*V); d[source] = 1; q = deque([source])
    while q:
        u = q.popleft()
        if u == sink: break
        for idx in AL[u]:
            v, c = divmod(EL[idx], K)
            if c > 0 and d[v] == 0: d[v] = 1; q.append(v); p[v] = idx
    if not d[sink]: break
    mf += 1; s = sink
    while s != source: EL[p[s]] -= 1; EL[p[s]^1] += 1; s = EL[p[s]^1]//K
print(mf)