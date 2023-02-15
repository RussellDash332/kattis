import sys

INF, n = float('inf'), -1
vals, el, tmp = [], [], []
for line in sys.stdin:
    if n == -1:
        n = V = int(line)
        v = -1
        vals.clear()
        el.clear()
        tmp.clear()
    elif n != 0:
        nums = list(map(int, line.split()))
        if v == -1:
            v, l, *nums = nums
            vals.append(v)
        tmp.extend(map(lambda x: (len(vals)-1, x-1), nums))
        if len(tmp) == l:
            el.extend(tmp)
            v = -1
            tmp.clear()
            n -= 1
        if n == 0:
            D = [INF]*V
            D[0], win = -100, 0
            for _ in range(V):
                if D[-1] != INF and D[-1] < 0:
                    win = 1
                    break
                for x, y in el:
                    new = D[x] - vals[y]
                    if new < 0 and new < D[y] and D[x] < 0: D[y] = new
            if not win:
                D2, stop = D.copy(), False
                for _ in range(V):
                    tmp = D2.copy()
                    for x, y in el:
                        new = tmp[x] - vals[y]
                        if new < 0 and new < tmp[y] and tmp[x] < 0: tmp[y] = new
                    for i in range(V):
                        if D2[i] == INF and tmp[i] != INF:
                            stop = True
                            break
                    if stop: break
                    D2 = tmp
                D2 = [D2[i] + ((D2[i]-D[i])*1e8 if D2[i] != INF else 0) for i in range(V)] # proof by AC?
                for _ in range(V):
                    if D2[-1] != INF and D2[-1] < 0:
                        win = 1
                        break
                    for x, y in el:
                        new = D2[x] - vals[y]
                        if new < 0 and new < D2[y] and D2[x] < 0: D2[y] = new
            print(['hopeless', 'winnable'][win])
            n = -1