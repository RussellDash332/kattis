from cmath import *
k, v = map(int, input().split())
f = 1<<k; p = [[0]*f for _ in range(v)]; p[0][0] = 1
precomp = [bin(i).count('1') for i in range(f)]
for t in range(v-1):
    pp, vv = map(float, input().split()); vv = int(vv)
    for i in range(f): p[t+1][(i+vv)%f] += p[t][i]*pp; p[t+1][i] += (1-pp)*p[t][i]

def fft(v, inv=False):
    n = len(v); j = 0; k = 2
    for i in range(1, n):
        b = n>>1
        while j&b: j ^= b; b >>= 1
        j ^= b
        if i < j: v[i], v[j] = v[j], v[i]
    wk = exp(1j*(1-2*inv)*pi)
    while k <= n:
        for i in range(0, n, k):
            w = 1
            for j in range(i, i+(k>>1)): y = v[j+(k>>1)]*w; v[j+(k>>1)] = v[j]-y; v[j] = v[j]+y; w *= wk
        k <<= 1; wk **= 0.5
    return v

fft1, fft2 = fft(p[-1]), fft(precomp)
prod = [t.real/f for t in fft([fft1[i]*fft2[i] for i in range(f)], inv=True)]
print(f-1-prod.index(min(prod)))