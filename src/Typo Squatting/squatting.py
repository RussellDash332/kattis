import sys; input = sys.stdin.readline; from array import *; from collections import *
N = int(input()); W = []; M = 10**18+7; P = 359; Z = array('i', [0]*N); C = [1]; p = 0
for x in range(N):
    S = input().strip(); L = len(S); h = 0; Z[x] = L
    while len(C) < L: C.append(C[-1]*P%M)
    for i in S: h = (h*P+ord(i))%M
    for i in range(L): W.append((h-ord(S[i])*C[~i+L])%M)
H = Counter(W)
for x in range(N):
    for _ in range(Z[x]): Z[x] -= H[W[p]]; p += 1
    sys.stdout.write(str(-Z[x])+' ')