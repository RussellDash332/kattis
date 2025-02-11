def convert(ip):
    if '.' in ip:
        # IPv4
        a, b, c, d = map(int, ip.split('.'))
        return convert(f'::ffff:{hex(256*a+b)[2:]}:{hex(256*c+d)[2:]}')
    else:
        # IPv6
        s = ip.split('::'); h = 0
        if len(s) == 1: z = s[0].split(':')
        elif s[0] == s[1] == '': z = ['0']*8
        elif s[0] == '': k = len(s[1].split(':')); z = ['0']*(8-k)+s[1].split(':')
        elif s[1] == '': k = len(s[0].split(':')); z = s[0].split(':')+['0']*(8-k)
        else: k = len(s[0].split(':'))+len(s[1].split(':')); z = s[0].split(':')+['0']*(8-k)+s[1].split(':')
        for x in z: h *= 65536; h += int(x, 16)
        return h
T = {}; D = {}
for _ in range(int(input())):
    l = input().split()
    if l[0] == '+':
        _, k, v = l
        if k not in T: T[k] = []
        D[k] = v
    elif l[0] == '-': _, k = l; T.pop(k); D.pop(k)
    elif l[0] == '=':
        _, ip1, ip2, k, v = l
        ip1 = convert(ip1); ip2 = convert(ip2)
        T[k].append((ip1, ip2, v))
    else:
        ip = convert(l[1])
        P = []
        for k in T:
            P.append((k, D[k]))
            for l, r, v in T[k][::-1]:
                if l <= ip <= r: P[-1] = (k, v); break
        print(len(P))
        for p in sorted(P): print(*p)