import sys; input = sys.stdin.readline; from bisect import *
for _ in range(int(input())):
    N = int(input()); L = [-1, *map(int, input().split())]; H = [10**9, *map(int, input().split())]; z = [None]*(N+1); s = []; Z = [0]*(N+1); P = [0]
    for i in H: P.append(P[-1]+i)
    for i in range(N, -1, -1):
        while s and H[s[-1]] < H[i]: z[s.pop()] = i
        s.append(i)
    for i in range(1, N+1): j = z[i]; Z[i] = Z[j]+min(H[i], H[j])*(L[i]-L[j]-1)-P[i]+P[j+1]
    for _ in range(int(input())): print(bisect(Z, int(input())-1)-1)