budget = [1500]
def get(i, aa=1):
    if data[i] != None: return data[i]
    if debug: budget[0] -= 1; assert budget[0] >= 0 # trigger RTE if over the budget
    print('Q', i+1); data[i] = int(input())
    if aa: found.append((data[i], i)), found.sort()
    return data[i]

from bisect import *
debug = False
c, a = map(int, input().split())
s = [*map(int, input().split())]
data = [None]*c; ans = [None]*a
found = [(-10**10, 0), (get(0, 0), 0), (get(c-1, 0), c-1), (10**10, c-1)]
for i in range(a):
    if s[i] >= data[-1]: ans[i] = c; continue
    lo, hi = found[bisect_left(found, (s[i], -1))-1][1], found[bisect_left(found, (s[i]+1, -1))][1]-1
    while hi>lo:
        mi = (lo+hi+1)//2
        if get(mi) == s[i]: lo = hi = mi; break
        elif get(mi) < s[i]: lo = mi
        else: hi = mi-1
    ans[i] = lo+1
if debug:
    for i in range(a):
        if (ans[i] == c or get(ans[i]) > s[i]) and get(ans[i]-1) <= s[i]: continue
        bomb = [10**9]*10**9 # trigger MLE if answer is not optimal
print('A', *ans) # trigger WA in any other cases