import sys; input = sys.stdin.readline
for _ in range(int(input())):
    C, R, T = map(int, input().split())
    M1 = [[*map(lambda x: int(x=='#'), input().strip())] for _ in range(R)][::-1]
    M2 = [[*map(lambda x: int(x=='#'), input().strip())] for _ in range(R)][::-1]
    X = [sum(map(sum, M2)), sum(map(sum, M1))]
    t, m = 0, M2; tt = [0, 0]; over = last = 0
    for _ in range(T):
        c, r = map(int, input().split())
        if not over:
            miss = m[r][c] == 0
            if not miss:
                m[r][c] = 0; X[t] -= 1
                if (not X[0])^(not X[1]) and not last: tt[t] += 1; t = 1-t; m = M1 if t else M2; last = 1
            else:
                tt[t] += 1; t = 1-t; m = M1 if t else M2
            if tt[0] == tt[1]:
                if not X[1] and X[0]: print('player two wins'); over = 1
                elif not X[0] and X[1]: print('player one wins'); over = 1
                elif X[0] == X[1] == 0: print('draw'); over = 1
    if not over:
        if not X[1] and X[0]: print('player two wins')
        elif not X[0] and X[1]: print('player one wins')
        else: print('draw')