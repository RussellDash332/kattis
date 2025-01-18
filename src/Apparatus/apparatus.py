from collections import *
n, m = map(int, input().split()); f = [1]; M = 1000003; z = 1
for i in range(1, 1002): f.append(f[-1]*i%M)
a = ['']*n; b = ['']*n
for _ in range(m):
    s = input(); t = input()
    for i in range(n): a[i] += s[i]; b[i] += t[i]
c = Counter(a)
if c != Counter(b): print(0), exit(0)
for i in c.values(): z = z*f[i]%M
print(z)