import sys; input = sys.stdin.readline
for _ in range(int(input())):
    r, c = map(int, input().split())
    g = [input().strip() for _ in range(r)]
    v = [[0]*c for _ in range(r)]
    for i in range(c): v[0][i] = int(g[0][i] != '#')
    for i in range(1, r):
        for j in range(c):
            if g[i][j] != '#': v[i][j] = v[i-1][j] + 1
    cnt = [0]*(r+c+1)
    for i in range(r):
        s = []
        for j in range(c):
            best = j
            while s and s[-1][1] > v[i][j]: best = min(best, s.pop()[0])                    # given the southeast corner (i, j), what's the best southwest corner
            if v[i][j] == 0: continue                                                       # this is done after the while loop because we have to discard the stack elements if there's a swamp in between
            if not s or j-s[-1][0]+s[-1][1] < j-best+v[i][j]: s.append((best, v[i][j]))     # found a rectangle with a larger perimeter
            cnt[j-s[-1][0]+s[-1][1]+1] += 1                                                 # height is s[-1][1], width is j-s[-1][0]+1
    for i in range(r+c+1):
        if cnt[i]: print(cnt[i], 'x', 2*i)