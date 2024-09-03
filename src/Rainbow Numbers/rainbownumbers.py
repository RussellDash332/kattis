import sys; sys.setrecursionlimit(10**5)
m = 998244353
a = [*map(int, input())]
b = [*map(int, input())]
a = [0]*(len(b)-len(a))+a
a[-1] -= 1; p = len(a)-1
while a[p] < 0: a[p] += 10; a[p-1] -= 1; p -= 1

def f(x):
    n = len(x)
    def bt(pos, prev, tie):
        if pos == n: return 1
        if tie: return pow(9, n-pos, m)
        s = 0
        for u in range(x[pos]):
            if u == prev: continue
            s += bt(pos+1, u, 1)
        if x[pos] != prev: s += bt(pos+1, x[pos], 0)
        return s%m
    return bt(0, -1, 0)%m
print((f(b)-f(a))%m)