from collections import *
n, m, k, *a = map(int, open(0).read().split()); h = Counter(a)
def g(v, p): s, r = divmod(v, p+1); return ((p+1-r)*s+r*(s+2))*(s+1)//2
Z = [10**18]*(k+1)*(m+1)
V = [g(h[i+1], j) for i in range(m) for j in range(k+1)]
for i in range(m+1):
    for j in range(k+1):
        if i == 0: Z[j] = 0; continue
        for l in range(j+1): Z[i*k+i+j] = min(Z[i*k+i+j], Z[(i-1)*(k+1)+j-l]+V[(i-1)*(k+1)+l])
print(Z[-1])