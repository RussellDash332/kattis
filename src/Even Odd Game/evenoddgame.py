n = int(input()); A = set(); B = set(); C = set()
for _ in range(n):
    k, v = input().split(); d = (k, v)
    if k == '+':
        if int(v)%2: B.add(d)
        else: A.add(d)
    elif int(v)%2: A.add(d)
    else: C.add(d)
s = int(input())%2; a, b, c = map(len, (A, B, C))
def f(a, b, c, s, p):
    return [(s+b)%2==p, p==0 or c==b%2==1][min(c,1)]
def do(a, b, c, s):
    if a and f(a-1, b, c, s, P^1)^1: print(*A.pop()); a -= 1
    elif b and f(a, b-1, c, s^1, P^1)^1: print(*B.pop()); b -= 1; s ^= 1
    else: print(*C.pop()); c -= 1; s = 0
    return a, b, c, s
if f(a, b, c, s, 1): print('me'); P = 1; a, b, c, s = do(a, b, c, s)
else: print('you'); P = 0
while a+b+c:
    k, v = input().split(); d = (k, v)
    if k == '+':
        if int(v)%2: b -= 1; B.remove(d); s ^= 1
        else: a -= 1; A.remove(d)
    elif int(v)%2: a -= 1; A.remove(d)
    else: c -= 1; C.remove(d); s = 0
    if a+b+c: a, b, c, s = do(a, b, c, s)