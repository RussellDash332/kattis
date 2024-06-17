import sys; input = sys.stdin.readline
n, k = map(int, input().split()); bad = {}; z = 0
def merge(intervals): h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else[min(a[0],b[0]),max(a[1],b[1])]; return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]
for _ in range(k):
    x, y, b = map(int, input().split()); r = int(b**(1/3)+1)
    for p in range(max(x-r, 0), min(x+r, n)+1):
        sq = eq = None
        for q in range(max(y-r, 0), min(y+r, n)+1):
            if abs(x-p)**3 + abs(y-q)**3 <= b: sq = q; break
        for q in range(min(y+r, n), max(y-r, 0)-1, -1):
            if abs(x-p)**3 + abs(y-q)**3 <= b: eq = q; break
        if sq != None:
            if p not in bad: bad[p] = []
            bad[p].append((sq, eq+1))
for i in bad:
    for j in merge(bad[i]): z += j[1]-j[0]
print((n+1)**2-z)