import sys; sys.setrecursionlimit(1005); input = sys.stdin.readline

def dfs(g2, el2, v, ans):
    g2[v].sort(key=lambda w: el2[(v, w)][-1], reverse=True)
    while g2[v]:
        w = g2[v].pop()
        el2[(v, w)].pop(), dfs(g2, el2, w, ans)
    ans.append(v)

for _ in range(int(input())):
    words = [input().strip() for _ in range(int(input()))]
    g, el = [[] for _ in range(26)], {}
    for i in words:
        s, e = ord(i[0])-97, ord(i[-1])-97
        g[s].append(e)
        if (s, e) not in el: el[(s, e)] = []
        el[(s, e)].append(i)
    for i in el: el[i].sort(reverse=True)
    uans = ''
    ctr2 = {i: len(g[i]) for i in range(26) if g[i]}
    for source in range(26):
        # DFS Hierholzer
        g2 = [i.copy() for i in g]
        el2 = {i:[*j] for i,j in el.items()}
        ans = []; dfs(g2, el2, source, ans)
        if len(ans) != len(words)+1: continue
        ans = ans[::-1]
        # Compare multiset
        ctr = {}
        for i in range(len(words)):
            s, e = ans[i], ans[i+1]
            if (s, e) not in el: break
            if s not in ctr: ctr[s] = 0
            ctr[s] += 1
        if ctr != ctr2: continue
        # Wrap-up
        uans = '.'.join(el[(ans[i], ans[i+1])].pop() for i in range(len(words))); break
    print(uans if uans else '***')