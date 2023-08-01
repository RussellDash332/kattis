from random import *
n, m = map(int, input().split())
ans = 0; size = [1]*n; parent = [*range(n)]

def find(i):
    global ans
    while parent[i] != i: i = parent[i]; ans += 1
    return i

def depth(i):
    ret = 0
    while parent[i] != i: i = parent[i]; ret += 1
    return ret

def union(i, j):
    find(i), find(j) # waste
    i = find(i); j = find(j)
    if size[i] < size[j]: (i, j) = (j, i)
    size[i] += size[j]
    parent[j] = i

def add(a, b): edges.remove((min(a, b), max(a, b))), union(a-1, b-1), print(a, b)
if n == 7:
    for a, b in [[1, 2], [3, 4], [5, 6], [5, 7], [6, 7], [2, 4], [4, 7], [2, 3], [4, 5], [4, 6]]: print(a, b)
else: # n = 100, m = 500
    edges = {(i, j) for i in range(1, 100) for j in range(i+1, 101)}
    base = [[1, 2], [3, 4], [5, 6], [5, 7], [6, 7], [2, 4], [4, 7]]
    for a, b in base: add(a, b)
    for a, b in [[x+7, y+7] for x, y in base]: add(a, b)
    add(4, 11)
    base = [[x+14, y+14] for x, y in base]
    for a, b in base: add(a, b)
    for a, b in [[x+7, y+7] for x, y in base]: add(a, b)
    add(18, 25), add(11, 25)
    base = [[x+14, y+14] for x, y in base]
    for a, b in base: add(a, b)
    for a, b in [[x+7, y+7] for x, y in base]: add(a, b)
    add(32, 39)
    base = [[x+14, y+14] for x, y in base]
    for a, b in base: add(a, b)
    for a, b in [[x+7, y+7] for x, y in base]: add(a, b)
    add(46, 53), add(39, 53), add(25, 53)
    base = [[x+14, y+14] for x, y in base]
    for a, b in base: add(a, b)
    for a, b in [[x+7, y+7] for x, y in base]: add(a, b)
    add(60, 67)
    base = [[x+14, y+14] for x, y in base]
    for a, b in base: add(a, b)
    for a, b in [[x+7, y+7] for x, y in base]: add(a, b)
    add(74, 81), add(67, 81)
    base = [[x+14, y+14] for x, y in base]
    for a, b in base: add(a, b)
    for a, b in [[92, 93], [94, 95], [96, 97], [98, 99], [93, 95], [97, 99], [99, 100], [93, 94], [95, 99]]: add(a, b)
    add(88, 95), add(81, 95), add(81, 94), add(53, 95)
    left = len(edges)-4450
    dmap = {}
    for i in range(n):
        d = depth(i)
        if not d: continue
        if d not in dmap: dmap[d] = []
        dmap[d].append(i+1)
    for d1, d2 in [[7, 6], [7, 5], [6, 6], [7, 4], [6, 5], [7, 3], [6, 4], [5, 5], [7, 2], [6, 3], [5, 4]]:
        for a in dmap[d1]:
            for b in dmap[d2]:
                try: add(a, b); left -= 1
                except: pass
                if left == 0: exit(0)
    assert 0, left