x, z, k = map(int, input().split()); x //= 25; z //= 25; lo = -1; hi = k+1
def f(n):
    l = h = x; l += k-n
    for _ in range(n):
        l = l*9//10; h = h*9//10
        if l == 0: break
    h += k-n
    return l<=z, z<=h
while lo+1 < hi:
    ll, hh = f(mi:=(lo+hi)//2)
    if ll and hh: print('biceps'); exit()
    if hh: lo = mi
    if ll: hi = mi
print('liar')