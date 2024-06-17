import sys; input = sys.stdin.readline; from math import *
def bezout(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bezout(b, a%b); return (q, p-a//b*q)
def crt(a, m, b, n):
    d = gcd(m, n); k = m*n//d; return (a-m*bezout(m, n)[0]*(a-b)//d)%k, k
for _ in range(int(input())):
    A, B = 0, 1; n = int(input()); m, c = [x-1 for x in map(int, input().split())], [x-1 for x in map(int, input().split())]; p = [*range(100)]; s = [x-1 for x in map(int, input().split())]
    for i in range(100): p[i] = s[i]
    for i in range(n):
        ss = m[i]; p1 = []
        while ss != c[i]: p1.append(ss); ss = p[ss]
        ss = p[ss]; p2 = [c[i]]
        while ss != c[i]: p2.append(ss); ss = p[ss]
        A, B = crt(A, B, len(p1), len(p2))
    print(A)