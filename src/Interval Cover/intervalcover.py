import sys
t = 0
for l in sys.stdin:
    if t == 0:      a, b = map(float, l.split()); t = 1
    elif t == 1:    n, t, ints = int(l), 2, []
    else:
        n -= 1
        x, y = map(float, l.split())
        ints.append((x, y, len(ints)))
        if n == 0:
            t = 0
            ints.sort()
            s, used, i = a, [], 0
            while s < b or not used:
                best = (s, -1)
                while i < len(ints) and ints[i][0] <= s: best = max(best, ints[i][1:3]); i += 1
                if best[1] == -1: used.clear(); break
                s = best[0]
                used.append(best[1])
            if not used: print('impossible')
            else: print(len(used)), print(*used)