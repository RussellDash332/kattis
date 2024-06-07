import sys; input = sys.stdin.readline; from array import *; from random import *; seed(69)

def bt(i, bm):
    if i == len(V): return 0
    ans = bt(i+1, bm)
    if C[V[i]]&bm == 0:
        new = S[V[i]]+bt(i+1, bm|G[V[i]])
        if new > ans: ans = new
    return ans

C = array('i', [1<<i for i in range(20)])
while (N:=int(input())):
    P = [[*map(int, input().split())] for _ in range(N)]; G = array('i', C); S = array('i', [P[i][0]*P[i][1] for i in range(N)]); A = B = 0
    for i in range(N):
        lx1, ly1, hx1, hy1 = P[i][2], P[i][3], P[i][0]+P[i][2], P[i][1]+P[i][3]
        for j in range(i+1, N):
            lx2, ly2, hx2, hy2 = P[j][2], P[j][3], P[j][0]+P[j][2], P[j][1]+P[j][3]
            if (lx1<=lx2<=hx1 or lx2<=lx1<=hx2) and (ly1<=ly2<=hy1 or ly2<=ly1<=hy2):
                if min(hx1, hx2)-max(lx1, lx2) and min(hy1, hy2)-max(ly1, ly2): G[i] |= C[j]; G[j] |= C[i]
    for i in range(N):
        if G[i] == C[i]: A += S[i]; B |= C[i]
    V = [i for i in range(N) if B&C[i]==0]; shuffle(V); print(A+bt(0, B))