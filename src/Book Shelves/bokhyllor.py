a, b, c = map(int, input().split())
s = int(input())

mem = {}
def f(a, b, c, r=0):
    if a==b==c==0: return int(r>0)
    tup = (a, b, c, r)
    if tup in mem: return mem[tup]
    ans = 1e9
    if a:
        if r <= s-1: ans = min(ans, f(a-1, b, c, r+1))
        else: ans = min(ans, 1+f(a-1, b, c, 1))
    if b:
        if r <= s-2: ans = min(ans, f(a, b-1, c, r+2))
        else: ans = min(ans, 1+f(a, b-1, c, 2))
    if c:
        if r <= s-3: ans = min(ans, f(a, b, c-1, r+3))
        else: ans = min(ans, 1+f(a, b, c-1, 3))
    mem[tup] = ans; return ans
print(f(a, b, c))