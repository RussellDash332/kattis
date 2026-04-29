from collections import *
s = input(); n = len(s)
C = Counter(ord(x)-97 for x in input())
p = [[0]*(n+1) for _ in range(26)]
for i in range(n):
    for j in range(26): p[j][i+1] = p[j][i]+(ord(s[i])-97==j)
b = [[10**9]*n for _ in range(26)]
for i in range(26):
    k = 0
    for j in range(n):
        while k<n and (k<j or p[i][k]-p[i][j]<C[i]): k += 1
        if p[i][k]-p[i][j]>=C[i] and k>=j: b[i][j] = k-j
z = min(max(b[j][i] for j in range(26)) for i in range(n))
print(z if z < 10**9 else -1)