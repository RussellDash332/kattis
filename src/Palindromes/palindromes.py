import sys; input = sys.stdin.readline
class FenwickTree:
    def __init__(self, n):
        self.ft = [0]*(n+1); self.n = n
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def get(self, idx):
        s = 0
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s

# Part 1: Manacher's algorithm
S = input().strip(); N = len(S); s = '@#'+'#'.join(S)+'#^'; p = [0]*(2*N+3); l = r = 1
for i in range(2*N+2):
    p[i] = max(0, min(r-i, p[l+r-i]))
    while s[i-p[i]] == s[i+p[i]]: p[i] += 1
    if i+p[i] > r: l = i-p[i]; r = i+p[i]
A = [p[2*i+2]//2 for i in range(N)]; B = [p[2*i+1]//2 for i in range(N)]

# Part 2: Math
# For any given query [L, R], assume M1 = (L+R)//2 and M2 = (L+R+1)//2
# We want to find the following:
# sum_[i = L..M1] min(A[i], i-L+1) + sum_[i = M1+1..R] min(A[i], R-i+1)
# + sum_[i = L+1..M2] min(B[i], i-L) + sum_[i = M2+1..R] min(B[i], R-i+1)
# This is equivalent to
# sum_[i = L..M1] (i+min(A[i]-i, 1-L)) + sum_[i = M1+1..R] (min(A[i]+i, R+1)-i)
# + sum_[i = L+1..M2] (i+min(B[i]-i, -L)) + sum_[i = M2+1..R] (min(B[i]+i, R+1)-i)
# Bring out the easy terms, we now have
# (M1+L)*(M1-L+1)//2 - (R-M1)*(R+M1+1)//2 + (M2-L)*(M2+L+1)//2 - (R-M2)*(R+M2+1)//2
# + sum_[i = L..M1] min(A[i]-i, 1-L) + sum_[i = M1+1..R] min(A[i]+i, R+1)
# + sum_[i = L+1..M2] min(B[i]-i, -L) + sum_[i = M2+1..R] min(B[i]+i, R+1)

# Part 3: Offline Fenwick tree
Pv = FenwickTree(N); Qv = FenwickTree(N); Xv = FenwickTree(N); Yv = FenwickTree(N); Pf = FenwickTree(N); Qf = FenwickTree(N); Xf = FenwickTree(N); Yf = FenwickTree(N); qp = []; qq = []; qx = []; qy = []; z = [0]*(m:=int(input()))
for i in range(N): qp.append((A[i]-i, i)); qq.append((A[i]+i, i)); qx.append((B[i]-i, i)); qy.append((B[i]+i, i))
for i in range(m): l, r = map(int, input().split()); l -= 1; r -= 1; m1 = (l+r)//2; m2 = (l+r+1)//2; qp.append((1-l, l, m1, i)); qq.append((r+1, m1+1, r, i)); qx.append((-l, l+1, m2, i)); qy.append((r+1, m2+1, r, i)); z[i] += (m1+l)*(m1-l+1)//2-(r-m1)*(r+m1+1)//2+(m2-l)*(m2+l+1)//2-(r-m2)*(r+m2+1)//2
for q, v, f in ((qp, Pv, Pf), (qq, Qv, Qf), (qx, Xv, Xf), (qy, Yv, Yf)):
    q.sort(key=lambda x: (x[0], len(x)))
    for i in q:
        if len(i) == 2: v.add(i[1], i[0]); f.add(i[1], 1)
        else: z[i[3]] += v.get(i[2]+1)-v.get(i[1])+i[0]*(i[2]-i[1]+1-f.get(i[2]+1)+f.get(i[1]))

# Part 4: Profit!
print(*z)