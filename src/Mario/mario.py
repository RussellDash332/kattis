import sys; input = sys.stdin.readline
for _ in range(int(input())):
    N, W = map(int, input().split()); B = [[*map(int, input().split())] for _ in range(N)]; X, D = [b[0] for b in B], [1]*N; x = 0
    for t in range(5*W*W//8):
        if x == W: break
        F = [0]*(W+1)
        for i in range(N):
            F[X[i]] |= D[i]>0; X[i] += D[i]
            if X[i] == B[i][0] or X[i] == B[i][1]: D[i] *= -1
        if F[x]: x += 1         # just move right
        elif not F[x-1]: x -= 1 # all boats bring you backward
    print([t, 'IMPOSSIBLE'][x < W])