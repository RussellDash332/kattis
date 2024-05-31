import sys; input = sys.stdin.readline
K = ((0, 1), (0, -1), (-1, 0), (1, 0)); R, C = map(int, input().split()); M = [input().strip() for _ in range(R)]; W = set()

def bt(r, c, p, h):
    p.append(M[r][c]); h.add(r*C+c)
    if len(p) <= 10: W.add(''.join(p))
    if len(p) != 10:
        for dr, dc in K:
            if R>r+dr>-1<c+dc<C and (r+dr)*C+c+dc not in h: bt(r+dr, c+dc, p, h)
    h.discard(r*C+c); p.pop()

p, h, w = [], set(), 0
for r in range(R):
    for c in range(C): bt(r, c, p, h)
for i in range(int(input())): w += input().strip() in W
print(w)