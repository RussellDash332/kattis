from bisect import *
L = 30000; M = 2*L
def cross(a, b):
    return (a//M-L)*(b%M-L)-(a%M-L)*(b//M-L)
def sub(a, b):
    return M*(a//M-b//M+L)+a%M-b%M+L
def simple(P):
    S = []; N = len(P); V = [False]*N; P = P+[P[i-1] for i in range(N)]
    for i in range(N):
        if P[i] > P[i+N]: P[i], P[i+N] = P[i+N], P[i]
    def check(i, j):
        if (c1:=cross(sub(P[i], P[i+N]), sub(P[i], P[j+N]))) < 0 or (c2:=cross(sub(P[j], P[j+N]), sub(P[j], P[i+N]))) > 0: return False
        return P[i] != P[j] if c1 or c2 else not cross(sub(P[i], P[i+N]), sub(P[j], P[j+N]))
    def cmp(i, j): cp = cross(sub(P[j], P[i]), sub(P[j], P[j+N])); return cp < 0 or cp == 0 and cross(sub(P[i], P[i+N]), sub(P[j], P[j+N])) < 0
    for i in sorted(range(2*N), key=lambda x: P[x]*2*N-x):
        if i < N:
            insort(S, i, key=lambda j: cmp(i, j)); V[i] = True; x = S.index(i)
            if x != 0 and check(S[x-1], i) or x != len(S)-1 and check(i, S[x+1]): return 0
        elif V[i-N]:
            S.pop(x:=S.index(i-N)); V[i-N] = False
            if x != 0 and x != len(S) and check(S[x-1], S[x]): return 0
    return 1
import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
while (N:=int(input())):
    P = []
    for _ in range(N): x, y = map(int, input().split()); P.append(M*(x+L)+y+L)
    sys.stdout.write('YNEOS\n\n'[1-simple(P)::2])