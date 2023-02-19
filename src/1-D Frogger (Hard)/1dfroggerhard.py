import sys
sys.setrecursionlimit(2*10**5)
from collections import Counter

'''
A good test case to debug stuff:
11
10 4 3 1 1 -5 2 1 -1 -2 -5
'''

n = int(input())
a = list(map(int, input().split()))

# Original graph + transpose of the graph
g, gt = {}, {}
for i in range(n):
    if 0 <= i+a[i] < n:
        if i not in g: g[i] = []
        if i+a[i] not in gt: gt[i+a[i]] = []
        g[i].append(i+a[i])
        gt[i+a[i]].append(i)

# DFS toposort
def topo(g, l=range(n)):
    K = []
    vis = set()
    def dfst(s):
        vis.add(s)
        if s in g:
            for v in g[s]:
                if v not in vis: dfst(v) 
        K.append(s)
    for i in l:
        if i not in vis: dfst(i)
    return K
K = topo(g)

# Get all SCCs to find cycle early, use transpose of graph
scc, v, si = [-1]*n, [0]*n, 0
def dfs(u):
    v[u], scc[u] = 1, si
    if u in gt:
        for w in gt[u]:
            if not v[w]: dfs(w)
for i in K[::-1]:
    if not v[i]:
        dfs(i)
        si += 1

# Compress g to sccg
sccg = {}
scc_cnt = {}
scc_cnt_dup = {}
for i, e in enumerate(scc):
    if e not in scc_cnt: scc_cnt[e], scc_cnt_dup[e] = set(), []
    scc_cnt[e].add(a[i])
    scc_cnt_dup[e].append(a[i])

vv = set()
for i in g:
    for j in g[i]:
        if scc[i] != scc[j]: sccg[scc[i]] = [scc[j]]
        vv.add(scc[i])
        vv.add(scc[j])

# Transpose the SCC graph
sccgt = {}
for i in sccg:
    if sccg[i][0] not in sccgt: sccgt[sccg[i][0]] = set()
    sccgt[sccg[i][0]].add(i)

# DFS on sccgt in topological order of sccg
# vis to handle visited SCCs so far
# vis2 to handle magic numbers visited so far
K, vis, vis2 = topo(sccg, vv), set(), {}
ans = [0]
def dfs2(u):
    vis.add(u)
    if u not in sccgt: return
    else:
        for v in sccgt[u]:
            # guarantees len(scc_cnt_dup[v]) == 1
            mag = scc_cnt_dup[v][0]
            ans[0] += len(vis2) - (mag in vis2) # double counting with self->self
            vis2[mag] += 1
            dfs2(v)
            vis2[mag] -= 1
            if vis2[mag] == 0: del vis2[mag]
for ss in K:
    if ss not in vis:
        vis2 = Counter(scc_cnt[ss]) # these are all the magic numbers so far
        dfs2(ss)

# ans[0] = what we get from x->y where they belong to different SCCs
# the extra = what we get from two nodes in the same SCC
print(ans[0] + sum(len(scc_cnt[v])*len(scc_cnt_dup[v]) for v in scc_cnt))