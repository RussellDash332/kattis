import sys; input = sys.stdin.readline; print = sys.stdout.write
R, C, D = map(int, input().split()); A = [[*map(int, input().split())] for _ in range(R)]; K = ((0, -1), (-1, 0), (0, 1), (1, 0))
for i in range(R):
    for j in range(C):
        m = 10**9; k = A[i][j]//D
        for di, dj in K:
            if R>i+di>-1<j+dj<C: m = min(m, A[i+di][j+dj]//D)
        if k <= m: print(' ')
        elif k == m+1: print('+')
        elif k == m+2: print('X')
        else: print('#')
    print('\n')