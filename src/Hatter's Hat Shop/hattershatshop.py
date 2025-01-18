import sys; input = sys.stdin.readline; from heapq import *; from bisect import *
N, M, K = map(int, input().split()); D = []; C = []; X = 10**9+7
for _ in range(M): d, c = map(int, input().split()); D.append(d); C.append(c)
P = [[] for _ in range(M)]; Z = 0; Q = []; A = [0]*M; S = [[0] for _ in range(M)]
for _ in range(N): t, s = map(int, input().split()); Z += s; P[t-1].append(C[t-1]-s)
for i in range(M):
    P[i].sort(reverse=True)
    for j in P[i]: S[i].append(S[i][-1]+j)
for i in range(M):
    dz = 0
    for x in P[i]: dz += min(x, D[i])
    Q.append(-dz*X+i)
heapify(Q)
while K and Q:
    # try to devise hat idx
    ndz, idx = divmod(heappop(Q), X)
    if not ndz: break
    # how many times can we upgrade
    u = max(min((P[idx][-1]-A[idx])//D[idx], K), 1)
    while P[idx] and P[idx][-1]-A[idx] <= D[idx]*u: P[idx].pop()
    A[idx] += D[idx]*u; K -= u; Z -= ndz*u; p, hi = 0, len(P[idx]); l = hi; z = D[idx]+A[idx]
    while p < hi:
        mi = (p+hi)//2
        if P[idx][mi] < z: hi = mi
        else: p = mi+1
    # -sum(min(P[idx][i]-A[idx], D[idx]) for i in range(len(P[idx])))
    # -sum(min(P[idx][i], A[idx]+D[idx])-A[idx] for i in range(len(P[idx])))
    # -sum(min(P[idx][i], A[idx]+D[idx]) for i in range(len(P[idx]))) + A[idx]*len(P[idx])
    # -((A[idx]+D[idx])*p + {P[idx][p] + P[idx][p+1] + ... + P[idx][len(P[idx])-1])} + A[idx]*len(P[idx])
    # -((A[idx]+D[idx])*p + {S[idx][len(P[idx])]-S[idx][p]}) + A[idx]*len(P[idx])
    heappush(Q, (-p*z-S[idx][l]+S[idx][p]+A[idx]*l)*X+idx)
print(Z)