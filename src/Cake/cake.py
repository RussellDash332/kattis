import sys; input = sys.stdin.readline
p, q, n = map(int, input().split()); r = [[] for _ in range(p)]
for _ in range(n): a, b = map(int, input().split()); r[a-1].append(b-1)
for i in r: i.sort()
sr = 0
while True:
    cr = sr
    while cr < p and not r[cr]: cr += 1
    if cr == p: break
    cr2 = cr+1
    while cr2 < p and not r[cr2]: cr2 += 1
    cs = cr if cr2 < p else p-1; x = 0
    for i in r[cr][:-1]: print(sr+1, x+1, cs+1, i+1); x = i+1
    if r[cr]: print(sr+1, x+1, cs+1, q)
    sr = cr+1
    if sr == p: break
print(0)