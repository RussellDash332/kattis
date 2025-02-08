N = int(input())
oo = []
oxo = []
o = []
ooo = []
oooo = []
x = []

for i in range(N):
    s = input()
    if s == '1111': oooo.append(s)
    elif s.count('1') == 3: ooo.append(s)
    elif '11' in s or s[0]==s[3]=='1': oo.append(s)
    elif s.count('1') == 2: oxo.append(s)
    elif '1' in s: o.append(s)
    else: x.append(s)

print('Yes')

v = 0
for a in range(1, N+1):
    if N%a == 0:
        b = N//a
        if a == b == 1: v |= len(oooo) == N == 1
        elif a == 1 or b == 1: v |= len(ooo) == 2 == N-len(oxo)
        else: v |= len(oo) == 4 and len(o) == 2*(a+b-4)
if 1-v: print('No\nNo'); exit()
print('Yes')

z = t = 0
for s in oooo+ooo+oo+oxo+o+x:
    for i in s: z += i=='0'; t += i=='2'
print('YNeos'[z!=t::2]), exit()