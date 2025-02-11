A = [0]*201; B = [0]*201
for i in range(int(input())):
    a, b = map(int, input().split()); A[a-50] += 1; B[b-50] += 1
    X = [*A]; Y = [*B]; M = 0
    while X and Y:
        if X[-1] == 0: X.pop(); continue
        if Y[-1] == 0: Y.pop(); continue
        u = min(X[-1], Y[-1])
        M = max(M, abs(len(X)-len(Y)))
        X[-1] -= u; Y[-1] -= u
    print(M)