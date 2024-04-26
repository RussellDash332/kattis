import sys; input = sys.stdin.readline
n = int(input()); w = [input().strip() for _ in range(n)]; S = set(); T = []
P = 31; M = 10**18+7; R = [[] for _ in range(n)]; E = [1]; ans = []
for _ in range(10**6): E.append(E[-1]*P%M)
for i in range(n):
    h = x = 0
    for j in range(len(w[i])): x = h; h *= P; h += ord(w[i][j]); h %= M; R[i].append((x-h)*E[len(w[i])-1-j]%M)
    S.add(h); T.append(h)
for i in range(n):
    ok = 0
    for j in range(len(w[i])):
        if (T[i]+R[i][j])%M in S: ok = 1; break
    if ok: ans.append(w[i])
if not ans: print('NO TYPOS')
else:
    for i in ans: print(i)