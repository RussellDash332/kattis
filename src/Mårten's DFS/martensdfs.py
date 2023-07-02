import sys
v, e = map(int, input().split())
g, dfs = [set() for _ in range(v)], []
for l in sys.stdin:
    if e: 
        a, b = map(int, l.split())
        e -= 1
        g[a].add(b), g[b].add(a)
    else: dfs = list(map(int, l.split()))
if len(dfs) != v: print('NO'), exit(0) # {*dfs} == {*range(v)} is stronger
vis, s = [1]*v, []
for i in range(v-1):
    if dfs[i+1] not in g[dfs[i]]:
        for u in g[dfs[i]]:
            if vis[u]: print('NO'), exit(0)
        while s and dfs[i+1] not in g[s[-1]]: s.pop()
    s.append(dfs[i]); vis[dfs[i]] = 0
print(['NO', 'YES'][sum(vis)==max(vis)])