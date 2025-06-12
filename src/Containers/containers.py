for _ in range(int(input())):
    s = input().split(); H = [0]*100
    qp, qv = map(int, s[-1])
    if not qp: qp = qv
    for i in range(len(s)-1):
        r = s[i]; k = r.find('-')
        if k == 0:
            p, v = map(int, r[1:3])
            if not p: p = v
            H[10*p+v] = p if H[10*p+v] < p else v
        elif len(r) == 3:
            p, v = map(int, r[:2])
            if not p: p = v
            H[10*p+v] = 0 if H[10*p+v] <= p else p
        else:
            sp, sv = map(int, r[:2]); dp, dv = map(int, r[3:5])
            if not sp: sp = sv
            if not dp: dp = dv
            ss = 10*sp+sv; dd = 10*dp+dv
            while H[ss] and dp <= H[dd] < dv: H[ss] -= 1; H[dd] += 1
            while H[ss] and H[dd] < dp: H[ss] -= 1; H[dd] += 1
    print(H[10*qp+qv])