import sys; input = sys.stdin.readline
n, k = map(int, input().split()); t = 1
if n < k: print('Neibb'), exit(0)
s = [*zip(*(map(int, input().split()) for _ in range(2)))]
f = sorted([i for i in s if i[0] == 4], key=lambda x: x[1], reverse=True)
s = sorted([i for i in s if i[0] > 4], key=lambda x: (x[1], x[0]), reverse=True)
while t <= k:
    if s and s[-1][1] == t:
        if f and f[-1][1] == t: s.pop(), f.pop(); t += 1; continue
        elif len(s) > 1 and s[-2][1] == t: s.pop(), s.pop(); t += 1; continue
    q = None
    while f:
        q, d = f.pop()
        if d < t: q = None
        else: break
    if q == None:
        while s:
            q, d = s.pop()
            if d < t: q = None
            else: break
        if q == None: print('Neibb'), exit(0)
    q2 = None
    while f and q > 4:
        q2, d = f.pop()
        if d < t: q2 = None
        else: break
    if q2 == None:
        while s:
            q2, d = s.pop()
            if d < t: q2 = None
            else: break
        if q2 == None: print('Neibb'), exit(0)
    t += 1
print('Jebb' if t > k else 'Neibb')