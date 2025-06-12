a, b, c, d = input().split(); c = int(c); d = int(d); xa = 1<<len(a); xb = 1<<len(b)
A = [''.join(a[j] for j in range(len(a)) if (1<<j)&i) for i in range(xa)]
B = [''.join(b[j] for j in range(len(b)) if (1<<j)&i) for i in range(xb)]
da = {A[i]: ''.join(sorted(A[~i])) for i in range(xa)}
db = {B[i]: ''.join(sorted(B[~i])) for i in range(xb)}
for x in da:
    if x and x!='0' and str(u:=int(x))==x and u*d%c==0 and (y:=str(u*d//c)) in db and da[x]==db[y]: print('possible', x, y); exit()
print('impossible')