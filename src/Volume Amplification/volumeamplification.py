import sys; input = sys.stdin.readline; from array import *
for _ in range(int(input())):
    a, y = map(int, input().split()); v = sorted(map(int, input().split())); dp = array('b', [0]*(y+1)); dp[1] = 1; p = 1
    for i in v:
        if p < y: p *= i
        for j in range(min(p, y)//i, -1, -1): dp[j*i] |= dp[j]
    for i in range(y, -1, -1):
        if dp[i]: print(i); break