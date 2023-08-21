import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    price = {}; pickup = {}; rate = {}; using = {}; consistent = {}; cost = {}
    for _ in range(n): N, *r = input().split(); price[N], pickup[N], rate[N] = map(int, r)
    for _ in range(m):
        _, p, e, r = input().split()
        if p not in cost: using[p], consistent[p], cost[p] = None, True, 0
        if e == 'p':
            if using[p] != None: consistent[p] = False
            if consistent[p]: c = r.strip(); cost[p] += pickup[c]; using[p] = c
        elif e == 'r':
            if using[p] == None: consistent[p] = False
            if consistent[p]: cost[p] += int(r)*rate[using[p]]; using[p] = None
        else:
            if using[p] == None: consistent[p] = False
            if consistent[p]: cost[p] += (int(r)*price[using[p]]+99)//100
    for p in using:
        if using[p] != None: consistent[p] = False
    for p in sorted(cost): print(p, cost[p] if consistent[p] else 'INCONSISTENT')