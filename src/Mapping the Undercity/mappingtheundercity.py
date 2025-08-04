import sys; input = sys.stdin.readline; from collections import *
N = int(input()); A = [*map(int, input().split())]; B = [*map(int, input().split())]; P = [(A[i], B[i]) for i in range(N)]; M = 10**9+7; Z = 1; H = {}; K = A[0]-B[0]
if A[0] or B[1] or A[1]*B[0] == 0 or A[1]-B[0] or A.count(0)-1 or B.count(0)-1: print(0); exit()
for a, b in P:
    if a-b not in H: H[a-b] = Counter()
    H[a-b][a] += 1
if any(h%2 != K%2 or h < K or h > -K for h in H): print(0); exit()
for h in range(K, -K+1, 2):
    if h not in H: print(0); exit()
    H[h] = sorted(H[h].items()); u, x = H[h][0]
    if x > 1 or h-2*u != K: print(0); exit()
    for i in range(len(H[h])-1):
        u, x = H[h][i]; v, y = H[h][i+1]
        if u+1 != v: print(0); exit()
        Z = Z*pow(x, y, M)%M
print(Z)