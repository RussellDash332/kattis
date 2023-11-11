from math import *
n = int(input()); q = []
def populate(idx, low, high):
    if low >= high: return
    mid = (low + high)//2
    if len(q) <= idx: q.append(set())
    for i in range(low, mid+1): q[idx].add(i)
    populate(idx+1, low, mid), populate(idx+1, mid+1, high)
populate(0, 1, n); full = {*range(1, n+1)}
possible = [2**n-1 for _ in range(n)]
for i in q:
    print('?', len(i), *i)
    ans = sum(map(lambda x: 1<<(int(x)-1), input().split()))
    for j in i: possible[j-1] &= ans
    for j in full-i: possible[j-1] &= ~ans
print('!', *[round(log2(i))+1 for i in possible])