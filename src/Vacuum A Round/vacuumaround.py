from math import *
oa = asin; asin = lambda x: oa(min(max(x, -1), 1))
R, N, K, C = map(int, input().split())
A = [float(input()) for _ in range(N)]
A += [x+2*pi for x in A]
a = asin(C/R); b = 2*asin(C/2/R); Z = 0
def f(t):
    return R*R*(t/2-sin(2*t)/4)-C*C*t/2+g(t)/2
def g(t):
    return R*sin(t)*max(0, C*C-R*R*sin(t)**2)**.5+C*C*asin(R*sin(t)/C)
fb = f(b); gb = g(b)
def h(t):
    if t <= b: return f(t)
    return fb+g(min(t, a))-gb
W = [0]*4*N*N
for j in range(2*N):
    for i in range(j): W[i*2*N+j] = 2*h((A[j]-A[i])/2)
for s in range(N):
    p = [0]+[-1e9]*~-N
    for c in range(2, K+1):
        q = [0]*N; t = [(c-1, N-1, c-2, N-2)]
        while t:
            l, r, l2, r2 = t.pop()
            if l > r: continue
            j = (l+r)>>1; v = -1e9; b = l2
            for i in range(l2, min(r2+1, j)):
                x = p[i]+W[(s+i)*2*N+s+j]
                if x > v: v, b = x, i
            q[j] = v; t += [(j+1, r, b, r2), (l, j-1, l2, b)]
        p = q
    for j in range(K-1, N): Z = max(Z, p[j]+W[(s+j)*2*N+s+N])
print(Z)