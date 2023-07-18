import sys; input = sys.stdin.readline
T = int(input())
MOD = 9901
facts = [1]; twopow = [1]
for i in range(1, 300): facts.append(facts[-1]*i%MOD)
for i in range(16): twopow.append(twopow[-1]*2%MOD)

def dfs(u, p=None):
    if not go[0]: return
    if vis[u]: go[0] = 0; return cc.append(u)
    vis[u] = 1
    cc.append(u)
    for v in al[u]:
        if v != p: dfs(v, u)

# https://stackoverflow.com/questions/4759955/how-do-i-find-the-number-of-hamiltonian-cycles-that-do-not-use-forbidden-edges
for t in range(1, T+1):
    ans = 0
    n, k = map(int, input().split())
    edges = [[*map(lambda x: int(x)-1, input().split())] for _ in range(k)]
    for x in range(1<<k):
        s = [edges[i] for i in range(k) if (1<<i)&x]
        deg = [0]*n; c = 1
        for u, v in s: deg[u] += 1; deg[v] += 1
        for i in deg:
            if i > 2: c = 0; break
        if c == 0: continue
        sole, cyc, path = [], [], []
        al = [[] for _ in range(n)]
        for u, v in s: al[u].append(v), al[v].append(u)
        vis = [0]*n
        for i in range(n):
            cc = []
            if vis[i] == 0:
                go = [1]; dfs(i)
                if len(cc) > 1:
                    if cc[0] == cc[-1]: cyc.append(cc); break
                    else: path.append(cc)
                else: sole.append(cc[0])
        if cyc: c = 2*(len(cyc[0]) == n+1)
        else: c = twopow[len(path)]*facts[len(path)+len(sole)-1]
        ans += c*(-1)**len(s)
    print(f'Case #{t}:', ans*4951%MOD) # 1/2 = 4951 mod 9901