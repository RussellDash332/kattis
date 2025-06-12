n, *a = map(int, open(0).read().split()); one = a.count(1); two = a.count(2); v = [*map(str, sorted(i for i in a if i > 2))]; ot = min(one, two); one -= ot; two -= ot
if one == 0: print('*'.join(v+['2']*two+['(1+2)']*ot))
else:
    ooo, one = divmod(one, 3); new = ['(1+2)']*ot+['(1+1+1)']*ooo
    if one == 1:
        if new: new[0] = new[0][:-1]+'+1)'
        elif v: v[0] = '('+v[0]+'+1)'
        else: v = ['1']
    print('*'.join(['(1+1)']*(one//2)+new+v))