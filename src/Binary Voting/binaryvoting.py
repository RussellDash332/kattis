from cmath import *
k, v = map(int, input().split())
f = 1<<k; p = [[0]*f for _ in range(v)]; p[0][0] = 1
precomp = [bin(i).count('1') for i in range(f)]
for t in range(v-1):
    pp, vv = map(float, input().split()); vv = int(vv)
    for i in range(f): p[t+1][(i+vv)%f] += p[t][i]*pp; p[t+1][i] += (1-pp)*p[t][i]

def fft(v, inv=False):
    stack = [(2*len(v), v)]; tmp = []
    while stack:
        nb, v = stack.pop(); n, b = nb//2, nb%2
        if b == 0:
            if n == 1: tmp.append(v)
            else: stack.append((2*n+1, v)), stack.append((n, v[1::2])), stack.append((n, v[::2]))
        else:
            yo, ye = tmp.pop(), tmp.pop(); y, wj = [0]*n, 1; w = exp(-1j*(2-4*inv)*pi/n)
            for i in range(n//2): y[i] = ye[i] + wj * yo[i]; y[i + n//2] = ye[i] - wj * yo[i]; wj *= w
            tmp.append(y)
    return tmp[0]

fft1, fft2 = fft(p[-1]), fft(precomp)
prod = [t.real/f for t in fft([fft1[i]*fft2[i] for i in range(f)], inv=True)]
print(f-1-prod.index(min(prod)))