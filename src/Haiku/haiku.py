n = int(input()); s = [input() for _ in range(n)]; p = [input() for _ in range(3)]; h = 1
for i in range(3):
    d = [set() for _ in range(len(p[i])+1)]; d[0] = {0}
    for j in range(1, len(p[i])+1):
        if p[i][j-1] == ' ': d[j] = {*d[j-1]}
        for ss in s:
            if len(ss) <= j and ss == p[i][j-len(ss):j]:
                for k in d[j-len(ss)]: d[j].add(k+1)
    h *= [5, 7, 5][i] in d[-1]
print(['come back next year', 'haiku'][h])