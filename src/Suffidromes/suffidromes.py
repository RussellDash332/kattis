import sys
def f(s):
    for i in range(len(s)//2):
        if s[i] != s[~i]: return 0
    return 1
for a in sys.stdin:
    a = a.strip(); b = input(); ok = 0; eq = 1
    if a == b: print('No solution.'); continue
    k = min(len(a), len(b))
    for i in range(k+1):
        x = f(a[i:]); y = f(b[i:])
        if x and not y: print(a[:i][::-1]); ok = 1; break
        if y and not x: print(b[:i][::-1]); ok = 1; break
        if x and y and not eq: print(min(a[:i][::-1], b[:i][::-1])); ok = 1; break
        if i < k: eq &= a[i] == b[i]
    if ok: continue
    if len(a)>len(b): a,b=b,a
    if b[len(a)]=='a': print('b'+a[::-1])
    else: print('a'+a[::-1])