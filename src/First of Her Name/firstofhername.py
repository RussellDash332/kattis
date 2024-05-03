import sys; input = sys.stdin.readline; from array import *
n, q = map(int, input().split()); par = array('i', [0]*(n+1)); rank = array('i', [0]*(n+1)); M = 1<<20
for i in range(1, n+1): a, b = input().split(); par[i] = int(b); rank[i] = ord(a)

# https://mailund.dk/posts/prefix-doubling-attemps/
# prefix doubling like suffix array
# initially, we compare the first characters first and sort the "names" based on that
# to break ties, we compare based on the next 1 character from the start
# then next 2, next 4, and so on
offset = 1; jump = array('i', par); S = array('b', rank); mr = 91
while offset <= n:
    v = []
    for i in range(n, -1, -1): v.append(((mr*rank[i]+rank[jump[i]])<<20)+i); jump[i] = jump[jump[i]]
    v.sort(); nr = 0
    # assign 1-2-2-3 ranks
    for i in range(n+1): nr += (i > 0 and v[i-1]>>20 != v[i]>>20); rank[v[i]%M] = nr
    mr = max(28, nr+1); offset <<= 1

# count sort the ranks
a = [[] for _ in range(mr)]; A = array('i')
for i in range(n+1): a[rank[i]].append(i)
for i in range(mr):
    for j in a[i]: A.append(j)

# check compare(sorted[x], query)
# remember that A[i] = k if the k-th name is the i-th smallest
def f(x):
    x = A[x]
    for i in s:
        if S[x] > i: return 1
        elif S[x] < i: return -1
        x = par[x]
    return 0

# find upper bound to which it works
# 11111.....11000...00
def bs(lo, hi, t):
    lo, hi = 0, n
    while hi-lo>1:
        mi = (lo+hi)>>1
        if f(mi) < t: lo = mi
        else: hi = mi-1
    return hi if f(hi) < t else hi-1

for _ in range(q): s = [*map(ord, input().strip())]; sys.stdout.write(str(bs(0, n+1, 1)-bs(0, n+1, 0))+'\n')