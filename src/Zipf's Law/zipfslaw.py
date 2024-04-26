import sys; input = sys.stdin.readline
while (n:=int(input() or 0)):
    c = {}
    while True:
        s = input().strip()
        if s == 'EndOfText': break
        if not s: continue
        t = []; u = []
        for i in s.lower():
            if 'a'<=i<='z': u.append(i)
            elif u: t.append(''.join(u)); u = []
        if u: t.append(''.join(u))
        for v in t:
            if v not in c: c[v] = 0
            c[v] += 1
    for i in sorted(w for w in c if c[w] == n) or ['There is no such word.']: print(i)
    print()