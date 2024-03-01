def assign():
    a = [-1]*c
    def bt(cc, x, r):
        a[cc] = x; r += 1
        for dd in g[cc]:
            if a[dd] == x: a[cc] = -1; r -= 1; return 0
        for dd in g[cc]:
            ok = 1
            if a[dd] == -1:
                ok2 = 0
                for y in range(4):
                    if x != y and bt(dd, y, r): ok2 = 1; break
                ok *= ok2
            if 1-ok: a[cc] = -1; r -= 1; return 0
        return 1
    for cc in range(c):
        if a[cc] == -1:
            if 1-bt(cc, 0, 0): return 0
    return max(a)+1

for _ in range(int(input())):
    c, b = map(int, input().split()); g = [[] for _ in range(c)]
    for _ in range(b): i, j = map(int, input().split()); g[i].append(j), g[j].append(i)
    print(assign() or 'many')