N, *S = map(int, open(0)); V = v = C = c = 0
for i in sorted(S)[::-1]:
    C += 1; c += i
    if c >= v: V += C; v += c; C = c = 0
print(V)