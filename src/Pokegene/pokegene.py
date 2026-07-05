import sys; input = sys.stdin.readline
N, Q = map(int, input().split())
W = [input().strip() for _ in range(N)]; M = 10**9+7
H = [[h:=0]+[h:=(67*h+ord(c))%M for c in w] for w in W]
S = sorted(range(N), key=lambda x: W[x])
R = [-1]*N
for i in range(N): R[S[i]] = i
for _ in range(Q):
    K, L = map(int, input().split()); P = sorted(map(lambda x: int(x)-1, input().split()), key=lambda x: R[x]); Z = 0
    for i in range(K-L+1):
        a = H[P[i-1]] if i else [0]
        b = H[P[i]]
        c = H[P[i+L-1]]
        d = H[P[i+L]] if i+L<K else [0]
        x = y = z = 0
        lo, hi = 0, min(len(a), len(b))-1
        while hi-lo>1:
            if a[mi:=(lo+hi)//2]==b[mi]: lo = mi
            else: hi = mi-1
        x = hi if a[hi]==b[hi] else hi-1
        lo, hi = 0, min(len(b), len(c))-1
        while hi-lo>1:
            if b[mi:=(lo+hi)//2]==c[mi]: lo = mi
            else: hi = mi-1
        y = hi if b[hi]==c[hi] else hi-1
        lo, hi = 0, min(len(c), len(d))-1
        while hi-lo>1:
            if c[mi:=(lo+hi)//2]==d[mi]: lo = mi
            else: hi = mi-1
        z = hi if c[hi]==d[hi] else hi-1
        Z += max(y-max(x, z), 0)
    print(Z)