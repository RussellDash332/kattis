n = int(input())
s = [*map(lambda x: int(x)%2, input().split())]
ans = 0
def f(a, b):
    if a == b: return t[a]
    tup = (a, b)
    if tup in mem: return mem[tup]
    mem[tup] = max(f(a, a)-f(a+1, b), f(b, b)-f(a, b-1))
    return mem[tup]
for i in range(n):
    mem = {}; t = s[i+1:]+s[:i]
    ans += s[i]%2>f(0, n-2)
print(ans)