import sys
from itertools import permutations

# cannot use RDP :(
pre = {'(': 0, '+': 1, '-': 1, '*': 2}
s, t, o = [], 0, []
for l in sys.stdin:
    t = 1-t
    if t: A = [*map(int, l.split())]
    else:
        exp = l.strip()
        pf = []
        for i in l.strip():
            if i.isalpha(): pf.append(i)
            elif i == '(': s.append(i)
            elif i == ')':
                while s and s[-1] != '(': pf.append(s.pop())
                if not s or s[-1] == '(': s.pop()
            else:
                while s and pre[i] <= pre[s[-1]]: pf.append(s.pop())
                s.append(i)
        v = [i for i in pf if i.isalpha()]
        works = 0
        for p in permutations(A[1:-1]):
            rev = {v[i]:p[i] for i in range(len(v))}
            for i in pf:
                if i.isalpha(): s.append(rev[i])
                else:
                    b, a = s.pop(), s.pop()
                    if i == '+': s.append(a+b)
                    elif i == '-': s.append(a-b)
                    else: s.append(a*b)
            if s.pop() == A[-1]: works = 1; break
        o.append('YES' if works else 'NO')
print('\n'.join(o))