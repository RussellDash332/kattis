import sys; input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip(); can = set()
    for fl in range(1, min(len(s), 5)+1):
        fd = int(s[:fl]); n, p = fd+1, fl; ok = 1; ms = []; lds = set()
        for ll in range(fl, min(len(s)-fl, 5)+1):
            ld = int(s[-ll:])
            if fd < ld: lds.add(ld)
        while p < len(s):
            t, u = str(n), str(n+1)
            if u == s[p:p+len(u)]: ms.append(n); n += 2; p += len(u)
            elif t != s[p:p+len(t)]: ok = 0; break
            else: n += 1; p += len(t)
        if n-1 in lds and ok:
            if len(ms) == 1: can.add(ms[0])
            if not ms: can |= {fd-1, n}
    if len(s) < 6: can |= {int(s)-1, int(s)+1}
    can -= {0, 10**5}; sys.stdout.write(str(len(can))+'\n'+' '.join(map(str, sorted(can)))+'\n')