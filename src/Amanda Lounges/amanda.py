import sys

n, m = map(int, input().split())
lounge = [None]*n + [0,0]
g = tuple([] for _ in range(n))
for line in sys.stdin:
    u, v, t = map(int, line.split())
    u, v = u-1, v-1
    if t in (0, 2):
        if lounge[u] not in (None, t//2) or lounge[v] not in (None, t//2):
            print('impossible')
            sys.exit(0)
        lounge[u] = lounge[v] = t//2
    else:
        g[u].append(v)
        g[v].append(u)

vis = []
def dfs(u, c):
    stack = [(u, c)]
    while stack:
        u, c = stack.pop()
        lounge[u] = c
        vis.append(2*u+c)
        lounge[n+c] += 1
        for v in g[u][::-1]:
            if lounge[v] == c:
                print('impossible')
                sys.exit(0)
            elif lounge[v] == None:
                stack.append((v, 1-c))

for i in range(n):
    if lounge[i] != None:
        dfs(i, lounge[i])

for i in range(n):
    if lounge[i] == None:
        vis = []
        lounge[-2] = lounge[-1] = 0
        dfs(i, 0)
        if lounge[-2] < lounge[-1]:
            for j in set(vis):
                lounge[j//2] = 1-j%2
lounge.pop()
lounge.pop()
print(sum(lounge))