n = int(input()); R = []; C = []
for i in range(n): r, c = map(int, input().split()); t = [r, c, i]; R.append(t); C.append(t)
R.sort(); C.sort(key=lambda x: (x[1], x[0])); rw = [0]*n
print(sum(abs(R[i][0]-i-1)+abs(C[i][1]-i-1) for i in range(n)))
for i in range(n):
    if C[i][1] < i+1: rw[C[i][2]] = 1
for i in range(n-1, -1, -1):
    if rw[C[i][2]]:
        for _ in range(i+1-C[i][1]): print(C[i][2]+1, 'R'); C[i][1] += 1
for i in range(n):
    if not rw[C[i][2]]:
        for _ in range(C[i][1]-i-1): print(C[i][2]+1, 'L'); C[i][1] -= 1
for i in range(n):
    d = R[i][0]-i-1
    if d > 0:
        for _ in range(d): print(R[i][2]+1, 'U'); R[i][0] -= 1
    else:
        for _ in range(-d): print(R[i][2]+1, 'D'); R[i][0] += 1