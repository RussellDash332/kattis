import sys; input = sys.stdin.readline; from bisect import *
N, Q = map(int, input().split()); A = [*map(int, input().split())]; O = [*A]; C = [1]*N
for i in range(N):
    while O[i]%2 == 0: O[i] >>= 1; C[i] *= 2
P = [p:=0, *(p:=p+i for i in C)]
for _ in range(Q): x = int(input())-1; print(O[bisect(P, x)-1] if x < P[-1] else -1)