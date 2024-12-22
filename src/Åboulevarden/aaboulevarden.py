import sys; input = sys.stdin.readline; from bisect import *
H = {}
for i in range(int(input())):
    s = input().strip()
    if s not in H: H[s] = []
    H[s].append(i)
for _ in range(int(input())):
    X, s = input().strip().split(); X = int(X)
    r = bisect_left(H[s], X); D = 10**9
    if r < len(H[s]): D = H[s][r]-X
    if r-1 < len(H[s]): D = min(D, H[s][r-1]-X, key=abs)
    print(D)