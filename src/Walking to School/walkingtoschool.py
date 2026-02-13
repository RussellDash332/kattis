for _ in range(int(input())):
    C, R = map(int, input().split()); R += 1; C += 1
    M = [input() for _ in range(R)]
    D = [[0]*C for _ in range(R)]; D[-1][0] = 1
    for r in range(R-2, -1, -1):
        if M[r][0] == '.': D[r][0] = 1
        else: break
    for c in range(1, C):
        if M[-1][c] == '.': D[-1][c] = 1
        else: break
    for r in range(R-2, -1, -1):
        for c in range(1, C):
            if M[r][c] == '.': D[r][c] = D[r][c-1]+D[r+1][c]
    print(D[0][-1])