from math import *

# String representation of polynomial
def rep(p):
    n = len(p)
    sb = []
    for i in range(n):
        if p[i] not in [-1, 1]:
            sb.append(str(p[i]))
        elif p[i] == -1:
            sb.append('-')
        if i > 0:
            sb.append(f'x^{i}')
        if i < n-1 and p[i+1] > 0:
            sb.append('+')
    return ''.join(sb).replace('^1','')

# FFT, handles both FFT and IFFT
def fft(coef, inverse=False):
    n = len(coef)
    if n == 1:
        return coef
    y_e, y_o = fft(coef[::2], inverse), fft(coef[1::2], inverse)
    y = [0]*n
    for i in range(n//2):
        wj = complex(cos((2-4*inverse)*pi*i/n), sin((2-4*inverse)*pi*i/n))
        y[i] = y_e[i] + wj * y_o[i]
        y[i + n//2] = y_e[i] - wj * y_o[i]
    return y

# Multiply two polynomials
# x^2 + 3x + 7 -> [7, 3, 1]
def mult(p1, p2):
    m = len(p1) + len(p2) - 1
    n = 2**(len(bin(m)) - 2)
    p1 = p1 + [0]*(n - len(p1))
    p2 = p2 + [0]*(n - len(p2))
    fft1, fft2 = fft(p1), fft(p2)
    return [t.real/n for t in fft([fft1[i]*fft2[i] for i in range(n)], inverse=True)][:m]
    
q = int(input())
for _ in range(q):
    input()
    p1 = list(map(int, input().split()))
    input()
    p2 = list(map(int, input().split()))
    m = mult(p1, p2)
    print(len(m) - 1)
    print(*list(map(round, m)))