import sys; input = sys.stdin.readline; from cmath import *
def fft(v, inv):
    stack = [(2*len(v), v)]; tmp = []
    while stack:
        nb, v = stack.pop(); n, b = divmod(nb, 2)
        if b == 0:
            if n == 1: tmp.append(v)
            else: stack.append((2*n+1, v)); stack.append((n, v[1::2])); stack.append((n, v[::2]))
        else:
            yo = tmp.pop(); ye = tmp.pop(); y = [0]*n
            for i in range(n//2): wj = exp(-1j*inv*i*pi/n); y[i] = ye[i]+wj*yo[i]; y[i+n//2] = ye[i]-wj*yo[i]
            tmp.append(y)
    return tmp[0]
def sq(p): n = 2**(len(bin(2*len(p)-1))-2); f = fft(p+[0]*(n-len(p)), 2); return [round(t.real/n) for t in fft([f[i]**2 for i in range(n)], -2)]
N = int(input()); p = max(A:={*map(int, input().split())}); P = sq(sq([i in A for i in range(p+1)])); print(4*p, 4*min(A), sum(i>0 for i in P), sum(A)*4/N)