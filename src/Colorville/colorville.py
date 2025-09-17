from bisect import *
while True:
    n, k, m = map(int, input().split())
    if n < 1: break
    s = input(); c = {}; p = [-1]*n; w = 1
    for i in range(k):
        if s[i] not in c: c[s[i]] = []
        c[s[i]].append(i)
    for i in range(m):
        t = input(); l = len(t)
        if t[0] not in c or (q:=bisect(c[t[0]], p[i%n]))+l > len(c[t[0]]) or c[t[0]][q+l-1] == k-1:
            if w: print('Player', i%n+1, 'won after', i+1, 'cards.'); w = 0
        else: p[i%n] = c[t[0]][q+l-1]
    if w: print('No player won after', m, 'cards.')