from fractions import *; from collections import *; d = -1; A = []
for _ in range(int(input())):
    s = input(); h = Counter(s)
    if s[-1] == '{': d += 1; A.append([h['t'], h['s'], d])
    else: A.append([h['t'], h['s'], d]); d -= 1
for k in range(1, 1001):
    V = [(k*t+s, d) for t, s, d in A]
    if any((v==0)^(d==0) for v, d in V): continue
    if len({Fraction(v, d) for v, d in V if v})<2: print(k), exit()
print(-1)