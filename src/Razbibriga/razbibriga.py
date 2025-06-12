import sys; input = sys.stdin.readline
N = int(input()); Z = 0; W = [0]*676
for _ in range(N): s = input().strip(); W[26*ord(s[0])+ord(s[-1])-1755] += 1
def ctr(t):
    h = {}
    for i in t:
        if i not in h: h[i] = 1
        else: h[i] += 1
    return h
for a in range(676):
    for b in range(676):
        z = 1
        for i, k in ctr((a//26*26+b//26, a//26*26+b%26, b//26*26+a%26, b%26*26+a%26)).items():
            for j in range(k): z *= W[i]-j
        Z += z
print(Z)