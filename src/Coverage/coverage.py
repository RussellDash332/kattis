from math import *; from collections import *; from bisect import *; from array import *
N = int(input()); T = [set() for _ in range(N)]; F = [set() for _ in range(N)]; P = [[*map(float, input().split())] for _ in range(N)]; C = array('h', [0]*N); c = 0
for k in range(2):
    A = array('h', sorted(range(N), key=lambda x: P[x][k]))
    for i in range(N):
        p = max(bisect(A, P[i][k]-4, key=lambda x: P[x][k])-1, 0)
        while p < N and P[A[p]][k] <= P[i][k]+4:
            l = A[p]; d = hypot(P[i][0]-P[l][0], P[i][1]-P[l][1])
            if d <= 2: T[i].add(l); T[l].add(i)
            elif d <= 4: F[i].add((l, d))
            p += 1
for i in range(N):
    if C[i] == 0:
        c += 1; s = [i]
        while s:
            u = s.pop()
            if C[u] == 0: C[u] = c; s.extend(T[u])
H = Counter(C); B = max(H.values())
for i in range(N):
    for j, d in F[i]:
        m = (P[i][0]+P[j][0])/2, (P[i][1]+P[j][1])/2
        n = sqrt(4-d*d/4)/d
        v = ((P[j][1]-P[i][1])*n, (P[i][0]-P[j][0])*n)
        for t in ((m[0]+v[0], m[1]+v[1]), (m[0]-v[0], m[1]-v[1])):
            u = {C[i], C[j]}; b = sum(H[c] for c in u)
            for k, _ in F[i]:
                if C[k] not in u and hypot(P[k][0]-t[0], P[k][1]-t[1]) <= 2: u.add(C[k]); b += H[C[k]]
            for k, _ in F[j]:
                if C[k] not in u and hypot(P[k][0]-t[0], P[k][1]-t[1]) <= 2: u.add(C[k]); b += H[C[k]]
            B = max(B, b)
print(B+1)