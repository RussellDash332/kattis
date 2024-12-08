from cmath import *
def fft(v, inv=False):
    stack = [(2*len(v), v)]; tmp = []
    while stack:
        nb, v = stack.pop(); n, b = nb//2, nb%2
        if b == 0:
            if n == 1: tmp.append(v)
            else: stack.append((2*n+1, v)), stack.append((n, v[1::2])), stack.append((n, v[::2]))
        else:
            yo, ye = tmp.pop(), tmp.pop(); y, wj = [0]*n, 1; w = exp(-1j*(2-4*inv)*pi/n)
            for i in range(n//2): y[i] = ye[i]+wj*yo[i]; y[i+n//2] = ye[i]-wj*yo[i]; wj *= w
            tmp.append(y)
    return tmp[0]

def mult(p1, p2):
    n = 2**(len(bin(m:=len(p1)+len(p2)-1))-2); fft1, fft2 = fft(p1+[0]*(n-len(p1))), fft(p2+[0]*(n-len(p2)))
    p = [round(t.real/n) for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]
    return p

n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
p = mult(a, b[::-1]); q = [0]*n
for i in range(len(p)): q[i%n] += p[i]
print(*([i for i in range(n)if q[(i-1)%n]==0]or[-1]))