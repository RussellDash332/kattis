import sys; N, *V = sys.stdin.read().split(); N = int(N); H = {}; C = [0]*676
for v in V:
    k = v[1:]
    if k not in H: H[k] = set()
    H[k].add(ord(v[0])-97)
for v in H.values():
    for i in v:
        for j in {*range(26)}-v: C[26*i+j] += 1
print(sum(C[26*i+j]*C[26*j+i] for i in range(26) for j in range(26)))