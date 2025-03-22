import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
for _ in range(int(input())):
    E, V, s, t = map(int, input().split()); s -= 1; t -= 1; G = []; D = [10**18]*V; D[s] = 0
    for _ in range(E): a, b, U = map(float, input().split()); G.append((int(a)-1, int(b)-1, -int(U*1000)))
    for _ in range(V-1):
        c = 1
        for a, b, w in G:
            if D[b]>D[a]+w: D[b] = D[a]+w; c = 0
        if c: break
    Z = 0; C = array('b', [0]*V); S = array('b', [0]*V)
    for a, b, w in G:
        if D[b]>D[a]+w: D[b] = D[a]+w; C[b] = D[b] < 10**13
    if C[t]: print('TRUE'); continue
    H = [[] for _ in range(V)]; T = array('h', [t])
    for a, b, _ in G: H[b].append(a)
    while T:
        u = T.pop()
        if C[u]: Z = 1; break
        if S[u] == 0: S[u] = 1; T.extend(H[u])
    print('FTARLUSEE'[Z::2])