import sys; input = sys.stdin.readline; from array import *
K = 17; n, q = map(int, input().split()); a = array('i', map(int, input().split())); p = array('i', [n]*(n+1)*K); s = []
for i in range(n):
    while s and a[s[-1]] <= a[i]: p[K*s.pop()] = i
    s.append(i)
for i in range(K-1):
    for j in range(n): p[K*j+i+1] = p[K*p[K*j+i]+i]
for _ in range(q):
    s, d = map(int, input().split()); s -= 1
    for i in range(K):
        if d&(1<<i): d ^= 1<<i; s = p[K*s+i]
    sys.stdout.write(str(s+1)+'\n' if s < n else 'leik lokid\n')