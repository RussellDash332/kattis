M = 998244353
precomp = {2**i:(pow(3, (M-1)>>i, M), pow(3, -((M-1)>>i), M))for i in range(19)} # 3 is a primitive root of M

def ntt(v, inv=False):
    stack = [(2*len(v), v)]; tmp = []
    while stack:
        nb, v = stack.pop(); n, b = nb//2, nb%2
        if b == 0:
            if n == 1: tmp.append(v)
            else: stack.append((2*n+1, v)), stack.append((n, v[1::2])), stack.append((n, v[::2]))
        else:
            yo, ye = tmp.pop(), tmp.pop(); y, wj = [0]*n, 1; w = precomp[n][inv]
            for i in range(n//2): y[i] = (ye[i]+wj*yo[i])%M; y[i+n//2] = (ye[i]-wj*yo[i])%M; wj *= w; wj %= M
            tmp.append(y)
    return tmp[0]

def mult(p1, p2):
    n = 2**(len(bin(m:=len(p1)+len(p2)-1))-2)
    p1 += [0]*(n-len(p1)); p2 += [0]*(n-len(p2))
    z = pow(n, -1, M); ntt1, ntt2 = ntt(p1), ntt(p2)
    p = [t*z%M for t in ntt([ntt1[i]*ntt2[i]%M for i in range(n)], inv=True)][:m]
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p

from collections import *
n, *a = map(int, open(0).read().split())
q = deque([[0]+[1]*i for i in sorted(a)])
while len(q) > 1: q.appendleft(mult(q.pop(), q.pop()))
print(*q[0][1:])