R, C = map(int, input().split())
M = [input() for _ in range(R)]
dr = 1; dc = 0
for i in range(R):
    for j in range(C):
        if M[i][j] == 'B': br, bc = i, j
while dr|dc:
    if M[br+dr][bc+dc] == '/':
        if dr == 1: br += 1; dr = 0; dc = -1
        elif dc == -1: bc -= 1; dc = 0; dr = 1
        else: bc += 1; dc = 0
    elif M[br+dr][bc+dc] == '\\':
        if dr == 1: br += 1; dr = 0; dc = 1
        elif dc == 1: bc += 1; dc = 0; dr = 1
        else: bc -= 1; dc = 0
    elif M[br+dr][bc+dc] == '.': br += dr; bc += dc
    elif M[br+dr][bc+dc] == '#':
        if dc: dc = 0; dr = 1
        else: dr = 0
    else: print('Ponnukaka'); exit() # S
print('Heill a hufi')