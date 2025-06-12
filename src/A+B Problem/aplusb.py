import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
offset = -min(min(arr), 0)

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

def sq(p):
    n = 2**(len(bin(m:=2*len(p)-1))-2); tmp = fft(p+[0]*(n-len(p)))
    return [round(t.real/n) for t in fft([tmp[i]**2 for i in range(n)], inv=True)][:m]

p = [0]*(max(arr)+offset+1)
for i in arr: p[i+offset] += 1
z, ans = p[offset], 0 # z for number of 0's

"""
Handle the polynomial this way
1 1 3 3 4 6 -> (2x + 2x^3 + x^4 + x^6)^2 - (2x^2 + 2x^6 + x^8 + x^12)   # remove double selection
            -> (2x^2 + 8x^4 + 4x^5 + 2x^6 + 8x^7 + 4x^9 + 2x^10)        # evaluate
            -> (8x^4 + 2x^6)                                            # keep related terms

In case of 0's, decrease ans by 2z(n-1)
"""

prod = sq(p)
while len(prod) < 2*len(p): prod.append(0)
for i in range(len(p)): prod[2*i] -= p[i]
ans -= 2*z*(n-1)

"""
(ai + x) + (aj + x) = (ak + x) + x

prod[i+offset] is now the number of ways we can sum two terms and obtain i+offset

Since the zero case is handled, we just need to handle RHS
which is how many such term with this value, p[i]
"""

for i in range(len(p)): ans += prod[i+offset]*p[i]
print(ans)