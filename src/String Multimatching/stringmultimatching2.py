from collections import deque
import sys
n, A = -1, 96
for s in sys.stdin:
    if n == -1:     n, c, pp = int(s), 0, []
    elif c != n:    pp.append(s.strip('\r\n')); c += 1
    else:
        s = s.strip('\r\n')
        a = [[[-1]*A, 0, -1, []]]
        for w in range(len(pp)):
            n = 0
            for i in range(len(pp[w])):
                idx = ord(pp[w][i])-32
                if a[n][0][idx] == -1: a[n][0][idx] = len(a); a.append([[-1]*A, 0, -1, []])
                n = a[n][0][idx]
            a[n][3].append(w); n = 0
        q = deque()
        for k in range(A):
            if a[0][0][k] == -1:    a[0][0][k] = 0
            elif a[0][0][k] > 0:    a[a[0][0][k]][1] = 0; q.append(a[0][0][k])
        while q:
            r = q.popleft()
            for k in range(A):
                arck = a[r][0][k]
                if arck != -1:
                    q.append(arck)
                    v = a[r][1]
                    while a[v][0][k] == -1: v = a[v][1]
                    a[arck][1] = a[arck][2] = a[v][0][k]
                    while a[arck][2] != -1 and not a[a[arck][2]][3]: a[arck][2] = a[a[arck][2]][2]
        # Aho-Corasick algorithm
        matches = [[] for _ in range(len(pp))]
        state = ss = 0
        for i in range(len(s)):
            idx = ord(s[i])-32
            while a[ss][0][idx] == -1: ss = a[ss][1]
            a[state][0][idx] = a[ss][0][idx]; state = a[state][0][idx]; ss = state
            while ss != -1:
                for w in a[ss][3]: matches[w].append(i+1-len(pp[w]))
                ss = a[ss][2]
            ss = state
        n = -1
        for i in matches: print(*i)