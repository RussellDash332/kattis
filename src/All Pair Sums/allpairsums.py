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

input(); a = [*map(int, input().split())]; b = [*map(int, input().split())]
p1 = [0]*(2*10**5+1); p2 = [0]*(2*10**5+1)
for i in a: p1[i+10**5] += 1
for i in b: p2[i+10**5] += 1
n = 2**(len(bin(m:=len(p1)+len(p2)-1))-2); fft1, fft2 = fft(p1+[0]*(n-len(p1))), fft(p2+[0]*(n-len(p2)))
p = [round(t.real/n) for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]
while len(p) > 1 and p[-1] == 0: p.pop()
p = {i:p[i] for i in range(len(p))}
for _ in range(int(input())): print(p.get(int(input())+2*10**5, 0))