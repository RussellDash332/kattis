N, M = map(int, input().split())
B = [[*input()] for _ in range(N)]
while True:
    found = False
    for i in range(N-2):
        for j in range(M-2):
            k = {B[i+p][j+q] for p in range(3) for q in range(3)}
            k.discard('?')
            if len(k) == 1 and k.pop() != 'W':
                found = True
                for p in range(3):
                    for q in range(3): B[i+p][j+q] = '?'
    if not found: break
for i in range(N):
    for j in range(M):
        if B[i][j] in 'RGB': print('NO'), exit(0)
print('YES')