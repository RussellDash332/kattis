from array import *
M = 10**9+7
K = 19*pow(20, -1, M)%M
P = array('I', [p:=1]+[p:=p*K%M for _ in range(10**5)])
G = array('I', [s:=0]+[s:=(s+p)%M for p in P])
L = array('I'); R = array('I'); LC = array('i'); RC = array('i'); S = array('I'); Z = array('I'); F = array('I')
def create(l, r):
    L.append(l); R.append(r); LC.append(-1); RC.append(-1); S.append(0); Z.append(1); F.append(0); return len(L)-1
def push(i):
    l = L[i]; r = R[i]
    if l == r: return
    mi = (l+r)>>1
    if LC[i] < 0: LC[i] = create(l, mi); RC[i] = create(mi+1, r)
    lc = LC[i]; rc = RC[i]; z = Z[i]; S[lc] = S[lc]*z%M; S[rc] = S[rc]*z%M; Z[lc] = Z[lc]*z%M; Z[rc] = Z[rc]*z%M; Z[i] = 1
import sys; input = sys.stdin.readline
input(); T = create(0, M)
for i in map(int, input().split()):
    x = M-i; stk = [(0, 0)]
    while stk:
        i, b = stk.pop()
        if b>0: S[i] = (S[lc:=LC[i]]+S[rc:=RC[i]]*P[F[lc]])%M; F[i] = F[lc]+F[rc]
        else:
            l = L[i]; r = R[i]
            if l > x or r < x: continue
            if l == r == x: F[i] += 1; S[i] = x*G[F[i]]%M; Z[i] = Z[i]*K%M; continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
    stk = [(0, 0)]; tmp = []
    while stk:
        i, b = stk.pop()
        if b>0: rs, rf = tmp.pop(); ls, lf = tmp.pop(); tmp.append(((ls+rs*P[lf])%M, lf+rf))
        else:
            l = L[i]; r = R[i]
            if l >= 0 and r <= M: tmp.append((S[i], F[i])); continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
    print(-tmp[0][0]%M)