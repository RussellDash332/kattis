for _ in range(int(input())):
    a, b, c, d, e = input().strip().split(); u = 5
    if a != '?': u -= 1; a = int(a)
    if b != '?': u -= 1; b = int(b)
    if c != '?': u -= 1; c = int(c)
    if d != '?': u -= 1; d = int(d)
    if e != '?': u -= 1; e = int(e)
    if not u: print(a, b, c, d, e)
    else:
        if a == '?' and d == '?':
            if b != '?' and c != '?': pass
            elif b != '?': c = e-3*b if e != '?' else 0
            elif c != '?': b = (e-c)//3 if e != '?' else 0
            else:
                for bc in range(10404):
                    b, c = bc//102, bc%102
                    if b+c<101 and e==3*b+c: break
            print(100, b, c, 0, 3*b+c)
        elif a == '?':
            if b != '?' and c != '?': pass
            elif b != '?': c = e-3*b if e != '?' else 0
            elif c != '?': b = (e-c)//3 if e != '?' else 0
            else:
                for bc in range(10404):
                    b, c = bc//102, bc%102
                    if b+c+d<101 and (e=='?' or e==3*b+c): break
            print(b+c+d, b, c, d, 3*b+c)
        elif d == '?':
            if b != '?' and c != '?': pass
            elif b != '?': c = e-3*b if e != '?' else 0
            elif c != '?': b = (e-c)//3 if e != '?' else 0
            else:
                for bc in range(10404):
                    b, c = bc//102, bc%102
                    if b+c<=min(a,100) and (e=='?' or e==3*b+c): break
            print(a, b, c, a-b-c, 3*b+c)
        else:
            if b != '?' and c != '?': pass
            elif b != '?': c = e-3*b if e != '?' else a-b-d
            elif c != '?': b = (e-c)//3 if e != '?' else a-c-d
            else:
                for bc in range(10404):
                    b, c = bc//102, bc%102
                    if b+c+d==a and (e=='?' or e==3*b+c): break
            print(a, b, c, d, 3*b+c)