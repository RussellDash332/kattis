import sys; input = sys.stdin.readline
from collections import defaultdict

def dfs(s):
    stack, vis = [s], set()
    alp = set()
    while stack:
        u = stack.pop()
        if u in vis: continue
        vis.add(u)
        for i in dic[u]:
            if i.isalpha(): alp.add(i)
            else: stack.append(i)
            if len(alp) > 1: return 0, 0
    if alp: dic[s] = alp; return 1, [*alp][0]
    dic[s] = {'x'}; return 1, 'x'

t = int(input())
for _ in range(t):
    a = input().split()
    b = input().replace('<', '(').split()
    if len(a) != len(b): print('-'); continue
    dic = defaultdict(lambda: set())
    for i in range(len(a)):
        if a[i][0] == '<': dic[a[i]].add(b[i])
        if b[i][0] == '(': dic[b[i]].add(a[i])
    c1, c2 = [], []
    consistent = 1
    for i in range(len(a)):
        if a[i][0] == '<':
            c, d = dfs(a[i])
            c1.append(d); consistent *= c
        else: c1.append(a[i])
        if not consistent: break
        if b[i][0] == '(':
            c, d = dfs(b[i])
            c2.append(d); consistent *= c
        else: c2.append(b[i])
        if not consistent: break
    if c1 != c2 or not consistent: print('-')
    else: print(' '.join(c1))