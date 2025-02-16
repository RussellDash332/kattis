N = int(input()); P = sorted([*map(int, input().split())] for _ in range(N)); E = {*range(2, 2*N+2, 2)}; F = {*range(2, 2*N+2, 2)}
for x, y in P: E.discard(y); F.discard(x)
if E: s = E.pop(); print('YES', *sum([(i+1, s//2) for i in range(N)], ())); exit()
if F: p = F.pop(); print('YES', *sum([(p//2, i+1) for i in range(N)], ())); exit()
if N == 1: print('NO'); exit()
s = P[0][1]; X = {(i, s//2) for i in range(2, N+1)}; P = {(x, y) for x, y in P}
for a in (1, 2):
    for b in (1, 2):
        if all((x+a, y+b) not in P for x, y in X) and (2*a, 2*b) not in P and (x, y) not in X: print('YES', *sum(X, ()), a, b); exit()