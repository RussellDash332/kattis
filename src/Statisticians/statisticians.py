from array import *; from bisect import *
T = 2000
H, W = map(int, input().split())
A, B = map(int, input().split())
M = [[*map(int, input().split())] for _ in range(H)]
V = [[0] for _ in range(H)]
Z = array('i', [0]*(10**4*T+1))
for i in range(H):
    for j in range(W): V[i].append(V[i][-1]+M[i][j])
S = [array('i', [0]*(W+1))]
for i in range(H):
    S.append(array('i', [0]))
    for j in range(W): S[-1].append(S[-2][j+1]+V[i][j+1])
for k in range(1, H+1):
    for l in range(max(1, A//k-1), min(W, B//k+1)+1):
        if A <= k*l <= B:
            for i in range(H-k+1):
                for j in range(W-l+1): Z[int(T*(S[i+k][j+l]-S[i][j+l]-S[i+k][j]+S[i][j])/k/l)] += 1
P = array('i', [0])
for i in Z: P.append(P[-1]+i)
if P[-1]%2: print((bisect(P, P[-1]//2)-1)/T)
else: print((bisect(P, P[-1]//2)+bisect(P, P[-1]//2-1)-2)/T/2)