from math import *
s = [*map(int, input())]; n = len(s); t = [n]*10; u = 0; d = n*(n+1)//2
for i in range(n-1, -1, -1):
    t[s[i]] = i
    q = sorted((t[j], j) for j in range(s[i]+1, 10) if t[j] != n); b = s[i]
    for j, k in q: u += b*(j-i); b = max(b, k); i = j
    u += b*(n-i)
g = gcd(u, d); u //= g; d //= g
print(f'{str(u//d)+" " if u//d else ""}{str(u%d)+"/"+str(d) if u%d else ""}' or '0')