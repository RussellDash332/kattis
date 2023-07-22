import string
import sys; input = sys.stdin.readline

def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else: g, y, x = egcd(b % a, a); return (g, x - (b // a) * y, y)

def inv_mod(a, m):
    g, x, _ = egcd(a, m)
    if g != 1: raise Exception
    else: return x % m

def mul(a, b):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][0]*b[0][j]
            for k in range(1, n): c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= 37
    return c

mem = {}
def det(a):
    if a in mem: return mem[a]
    s = 0; n = len(a)
    if n == 1: mem[a] = a[0][0]; return mem[a]
    if n == 2: mem[a] = a[0][0]*a[1][1]-a[1][0]*a[0][1]; return mem[a]
    if n == 3: mem[a] = a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1]) - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0]) + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]); return mem[a]
    for i in range(n):
        if a[0][i] == 0: continue
        s += a[0][i]*(-1)**i*det(tuple(tuple(a[j][k] for k in range(n) if k != i) for j in range(1, n)))
    mem[a] = s; return s

def inv(a):
    D = inv_mod(det(a)%37, 37)
    if len(a) == 1: return [[D]]
    return [[(-1)**(i+j)*det(tuple(tuple(a[k][l] for l in range(len(a)) if l != j) for k in range(len(a)) if k != i))*D%37 for i in range(len(a))] for j in range(len(a))]

rt = dict(enumerate(string.ascii_uppercase+'0123456789 '))
tr = {e:i for i,e in rt.items()}
n = int(input())
s = input().strip('\r\n'); t = input().strip('\r\n')
ss = [tr[i] for i in s]; tt = [tr[i] for i in t]
ss2, tt2 = [], []
seen = set()
for i in range(len(s)//n):
    tup = (tuple(ss[n*i:n*i+n]), tuple(tt[n*i:n*i+n]))
    if tup in seen: continue
    seen.add(tup), ss2.extend(tup[0]), tt2.extend(tup[1])
ss, tt = ss2, tt2
cuts = [[[j] for j in ss[n*i:n*i+n]] for i in range(len(ss)//n)]; cutt = [[[j] for j in tt[n*i:n*i+n]] for i in range(len(tt)//n)]
for cs, ct in zip(cuts, cutt):
    if sum(map(sum, cs)) == 0 != sum(map(sum, ct)): print('No solution'), exit(0) # zero matrix issue
packs = [tuple(zip(*[[k[0] for k in j] for j in cuts[n*i:n*i+n]])) for i in range(len(cuts)//n)]
packt = [tuple(zip(*[[k[0] for k in j] for j in cutt[n*i:n*i+n]])) for i in range(len(cutt)//n)]
if len(s) < 2*n**2: packs += [tuple(zip(*[[k[0] for k in j] for j in cuts[len(cuts)-n*i-n:len(cuts)-n*i]])) for i in range(len(cuts)//n)]; packt += [tuple(zip(*[[k[0] for k in j] for j in cutt[len(cutt)-n*i-n:len(cutt)-n*i]])) for i in range(len(cutt)//n)]
mats = []
for a, b in zip(packs, packt):
    if not mats:
        try: mats.append(mul(b, inv(a)))
        except: pass
    elif mul(mats[0], a) != [[*i] for i in b]: print('No solution'), exit(0)
if not mats:
    m = {}
    for i in range(len(s)//n):
        if (p:=s[n*i:n*i+n]) not in m: m[p] = t[n*i:n*i+n]
        elif t[n*i:n*i+n] != m[p]: print('No solution'), exit(0)
    print('Too many solutions')
else:
    for r in mats[0]: print(*r)