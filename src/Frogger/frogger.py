from collections import *
K = ((-1, 0), (0, -1), (0, 0), (0, 1), (1, 0))
def solve():
    X = int(input()); R, C = map(int, input().split()); G = input().index('G'); M = [set() for _ in range(R+2)]
    for i in range(1, R+1):
        m = input()
        for j in range(C): m[j] == 'X' and M[i].add(j)
    Q = deque([(R+1, input().index('F'), 0)]); R += 2; V = set()
    while Q:
        r, c, t = Q.popleft()
        if r == 0 and c == G: return t
        if t == X: continue
        if (u:=(X+1)*(r*C+c)+t) in V: continue
        V.add(u)
        for dr, dc in K:
            if R>r+dr>-1<c+dc<C:
                d = (R-1-r-dr)%2*2-1
                if (c+dc-d*(t+1))%C in M[r+dr]: continue
                Q.append((r+dr, c+dc, t+1))
    return 0
for _ in range(int(input())): t = solve(); print(f'The minimum number of turns is {t}.' if t else f'The problem has no solution.')