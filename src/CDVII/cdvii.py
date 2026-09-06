H = [*map(int, input().split())]
R = {}
while 1:
    try: p, t, c, k = input().split()
    except: break
    if p not in R: R[p] = []
    k = int(k); h = int(t.split(':')[2])
    R[p] += [(t, h, c, k)]
for p in sorted(R):
    R[p].sort(); z = 200
    for i in range(len(r:=R[p])-1):
        if r[i+1][2] != 'enter' == r[i][2]: z += 100+abs(r[i+1][3]-r[i][3])*H[r[i][1]]
    if z > 200: print(p, f'$%.2f'%(z/100))