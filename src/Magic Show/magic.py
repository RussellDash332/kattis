import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import *
N, K = map(int, input().split())
L = [*map(int, input().split())]
R = [*map(int, input().split())]
D = [[0]*(K+1) for _ in range(N+1)]
Z = []
for i in range(1, N+1):
    l = L[i-1]; r = R[i-1]; m = (l+r)//2
    E = [max(abs(k-m)*(l<=k<=r), abs(-k-m)*(l<=-k<=r)) for k in range(K+1)]
    if max(E) == 0: D[i] = [*D[i-1]]; continue
    m = [0]+[E[t]-E[t-1] for t in range(1, K+1)]; S = []; t = 0
    while t <= K:
        if t == K: u = K
        else:
            s = m[t+1]; u = t+1
            while u <= K and m[u] == s: u += 1
            u -= 1
        a = 0 if t == u else m[t+1]; S.append((t, u, a, E[t]-a*t)); t = u+1
    for x, y, a, c in S:
        q = deque(); rr = -1
        for j in range(K+1):
            l = max(j-y, 0); r = min(j-x, K)
            if l > r:
                while q and q[0][1] < l: q.popleft()
                rr = r; continue
            while rr < r:
                v = D[i-1][rr:=rr+1]-rr*a
                while q and q[-1][0] <= v: q.pop()
                q.append((v, rr))
            while q and q[0][1] < l: q.popleft()
            if q: D[i][j] = max(D[i][j], a*j+c+q[0][0])
print(D[N][a:=max(range(K+1), key=lambda x:D[N][x])])
for i in range(N-1, -1, -1):
    l = L[i]; r = R[i]; m = (l+r)//2; k = 0
    for j in range(a+1):
        if l<=j<=r and D[i+1][a] == D[i][a-j]+abs(j-m): a -= j; k = j; break
        if l<=-j<=r and D[i+1][a] == D[i][a-j]+abs(-j-m): a -= j; k = -j; break
    Z.append(k)
print(*Z[::-1])