import sys; input = sys.stdin.readline; from array import *
def add(i, j): M[j] or G[i].append(j)
for _ in range(int(input())):
    R, C = map(int, input().split()); C *= 2; M = array('b')
    for _ in range(R): M.extend(map(int, input().strip()))
    G = [[] for _ in range(R*C)]
    for i in range(R):
        for j in range(C//2):
            for k in range(2):
                p = i*C+2*j+k
                if M[p]: continue
                add(p, p^1)
                if (i+j)%2:
                    if j > 0: add(p, p-k-1)
                    if j < C//2-1: add(p, p-k+2)
                    if k and i < R-1: add(p, p-k+C); add(p, p-k+C+1)
                    elif k^1 and i > 0: add(p, p-k-C); add(p, p-k-C+1)
                else:
                    if i > 0: add(p, p-k-C+1)
                    if i < R-1: add(p, p-k+C)
                    if k and j < C//2-1: add(p, p-k+2); add(p, p-k+3)
                    elif k^1 and j > 0: add(p, p-k-2); add(p, p-k-1)
    V = array('b', [0]*R*C); P = 10**9
    # left border: (i%2 or k==0) and j==0
    # right border: ((i+j)%2 or k==1) and j==C//2-1
    # up border: (j%2==0 or k==0) and i==0
    # down border: ((i+j)%2==0 or k==1) and i==R-1
    def get(u):
        i = u//C; j = u%C//2; k = u%2
        return ((i%2 or k==0) and j==0)|(2*(((i+j)%2 or k==1) and j==C//2-1))|(4*((j%2==0 or k==0) and i==0))|(8*(((i+j)%2==0 or k==1) and i==R-1))
    for i in range(R*C):
        if V[i] == 0:
            Q = [i]; B = get(i); V[i] = 1
            for u in Q:
                for v in G[u]:
                    if V[v] == 0: V[v] = 1; Q.append(v); B |= get(v)
            if B == 15:
                Z = 1
                for u in Q:
                    if len(G[u]) == 1 or len(G[u]) >= 3 or get(u):
                        X = set()
                        for v in Q:
                            if u == v: continue
                            break
                        S = [v]; X.add(v); B = get(v)
                        for x in S:
                            for y in G[x]:
                                if y not in X and y != u: X.add(y); S.append(y); B |= get(y)
                        if B == 15: Z = 0; break
                if Z: P = min(P, len(Q))
    print(['NO MINIMAL CORRIDOR', P][P < 10**9])