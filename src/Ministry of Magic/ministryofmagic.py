import sys; input = sys.stdin.readline
C, P = map(int, input().split()); l = [1]*(C+1)
p = [[*map(int, input().split())][::-1] for _ in range(P)]
v = [p[i].pop() for i in range(P)]
c = {i:0 for i in {*(q[-1] for q in p)}}
for k in c: l[k] = 0
for _ in range(len(c)-1):
    for k in c: c[k] = 0
    for i in range(P):
        q = p[i]
        while l[q[-1]]: q.pop()
        c[q[-1]] += v[i]
    x = min(c.items(), key=lambda x: 2*C*x[1]+x[0])[0]
    l[x] = 1; del c[x]
for i in range(1, C+1):
    if l[i] == 0: print(i), exit(0)