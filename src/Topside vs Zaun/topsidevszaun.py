from random import *; from array import *
N, *A = map(int, open(0).read().split())
L = max(A)+1; M = 2*L+1 # allow sum deviation to be [0,2*L]-(L) instead of sum(A)//2, count deviation to be [0,N]-(N//2)
D = array('I', [0]*(N+1)*M); E = array('I', D); shuffle(A); Q = {(N//2)*M+L}
for i in A:
    U = set()
    for u in Q:
        t, s = divmod(u, M); U.add(u); E[u] = max(E[u], D[u])
        if -1<s+i<M>-1<t+1<N+1: U.add(k:=(t+1)*M+s+i); E[k] = max(E[k], D[u]+1)
        if -1<s-i<M>-1<t-1<N+1: U.add(k:=(t-1)*M+s-i); E[k] = max(E[k], D[u]+1)
    for u in U: D[u] = E[u]; E[u] = 0
    Q = U
print(D[(N//2)*M+L]//2 or -1)