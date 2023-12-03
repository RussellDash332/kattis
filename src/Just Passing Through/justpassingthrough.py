import sys; input = sys.stdin.readline; from array import *
r, c, n = map(int, input().split()); S = r*c; V = (n+1)*S; INF = 10**7; D = array('i', [INF]*V); m = [array('i', map(int, input().split())) for _ in range(r)]; rr = range(-1, 2); q = [c*i for i in range(r) if m[i][0]>=0]; s = array('b', [0]*V)
for i in range(r):
    if m[i][0]+1: D[c*i] = 0
while q:
    q2 = []
    for u in q:
        if s[u]: continue
        s[u] = 1; k, i, j = u//S, u%S//c, u%S%c; h = []
        if j < c-1:
            if 0<i<r-1 and j and m[i-1][j]>m[i][j]>m[i][j-1]>=0 and m[i+1][j]>m[i][j]>m[i][j+1]>=0:
                if k < n:
                    for di in rr:
                        if m[i+di][j+1]+1: h.append(((u+S+di*c+1)<<10)|m[i][j])
            else:
                for di in rr:
                    if 0<=i+di<r and m[i+di][j+1]+1: h.append(((u+di*c+1)<<10)|m[i][j])
        for vw in h:
            v, w = vw>>10, vw&1023
            if D[u] + w < D[v]: D[v] = D[u] + w; q2.append(v)
    q = q2
print(ans if (ans:=min(D[n*S+c*i+c-1]+m[i][-1] for i in range(r))) < INF else 'impossible')