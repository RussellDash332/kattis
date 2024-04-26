nets = [
    [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 1), (3, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)],
    [(0, 1), (1, 0), (1, 1), (2, 1), (2, 2), (3, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1)]
]

def rotate(net):
    m = max(n[1] for n in net)
    return [(-j+m, i) for i, j in net]

def flipv(net):
    m = max(n[0] for n in net)
    return [(-i+m, j) for i, j in net]

def fliph(net):
    m = max(n[1] for n in net)
    return [(i, -j+m) for i, j in net]

m = [input().strip() for _ in range(6)]
for net in nets:
    for _ in range(2):
        net = flipv(net)
        for _ in range(2):
            net = fliph(net)
            for _ in range(4):
                net = rotate(net)
                for oi in range(-4, 5):
                    for oj in range(-4, 5):
                        ok = 0
                        for i, j in net: ok += 6>i+oi>-1<j+oj<6 and m[i+oi][j+oj]=='#'
                        if ok == 6: print('can fold'), exit(0)
print('cannot fold')