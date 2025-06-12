n, s, *w = map(int, open(0).read().split()); w.sort()
if s == 1 or n == 1: print(1); exit()
def f(k):
    a = [[], [], []]
    for i in range(k): a[w[i]%3].append(w[i])
    z = sum(a[0])//3
    while a[1] and a[2]: z += (a[1].pop()+a[2].pop())//3
    while len(a[1]) > 1: z += (a[1].pop()+a[1].pop()+1)//3
    while a[1]: z += a[1].pop()//3+1
    while a[2]: z += a[2].pop()//3+1
    return z <= s-2
lo, hi = 0, n-2
while hi-lo>1:
    if f(mi:=(lo+hi)//2): lo = mi
    else: hi = mi-1
print(2+(hi if f(hi) else hi-1))