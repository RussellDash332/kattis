V, E = map(int, input().split())
g = [[] for _ in range(V)]
for _ in range(E):
    a, b = map(int, input().split())
    g[a-1].append(b-1); g[b-1].append(a-1)
ans, idx, stack = [], [0]*V, [0]
while stack:
    u = stack[-1]
    if idx[u] < len(g[u]):  stack.append(g[u][idx[u]]); idx[u] += 1
    else:                   ans.append(u), stack.pop()
while ans: print(ans.pop()+1)