import sys
I = {}; F = []
for l in sys.stdin:
    l = l.rstrip()
    if not l: break
    I[l] = []
for l in sys.stdin:
    l = l.rstrip(); f = l
    for _ in range(2): f = f[:f.rfind('_')]
    if f not in I: F.append(l)
    else: I[f].append(l)
tog = 1
for i in sorted(F): print('F', i); tog = 0
for i in sorted(I):
    if not I[i]: print('I', i); tog = 0
if tog: print('No mismatches.')