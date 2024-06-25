import sys; input = sys.stdin.readline; from array import *
while True:
    R, C, N = map(int, input().split())
    if R < 1: break
    Z = 0; D = array('b', [1]*R); E = array('b', [1]*C); F = array('b', [1]*(R+C)); G = array('b', [1]*(R+C))
    for _ in range(N): r, c = map(int, input().split()); r -= 1; c -= 1; D[r] = 0; E[c] = 0; F[r+c] = 0; G[r-c+C] = 0
    E = array('h', (i for i in range(C) if E[i]))
    for r in array('h', (i for i in range(R) if D[i])):
        for c in E:
            if F[r+c] and G[r-c+C]: Z += 1
    print(Z)