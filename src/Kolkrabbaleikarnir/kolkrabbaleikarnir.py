from math import *
n, m = map(int, input().split())
c = [0]; ans = 0
for i in range(min(n, m)):
    c.append(c[-1]+log2(n-i)-log2(i+1))
    if c[-1] < -1e-7: c.pop(); break
for k in range(m-len(c)+1, m+1): ans += k*2**(c[m-k]-n)
print(ans)