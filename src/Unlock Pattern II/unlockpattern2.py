s = input()
turn = [[[None]*9 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if i == j: continue
        for k in range(9):
            if k == i or k == j: continue
            aa, bb, cc, dd = j//3-i//3, j%3-i%3, k//3-j//3, k%3-j%3
            if (cross:=aa*dd-bb*cc) > 0:    turn[i][j][k] = 'L'
            elif cross < 0:                 turn[i][j][k] = 'R'
            elif (dot:=aa*cc+bb*dd) > 0:    turn[i][j][k] = 'S'
            else:                           turn[i][j][k] = 'A'

jump = [[None]*9 for _ in range(9)]
jump[2][6] = jump[6][2] = jump[0][8] = jump[8][0] = jump[3][5] = jump[5][3] = jump[1][7] = jump[7][1] = 4
jump[0][2] = jump[2][0] = 1
jump[6][8] = jump[8][6] = 7
jump[0][6] = jump[6][0] = 3
jump[2][8] = jump[8][2] = 5

# itertools.permutations will TLE, you can prune using recursion
ans = [0]
def solve(used=[0]*9, p=[]):
    if len(p) == 9:
        ok = 1
        for i in range(7):
            if s[i] == '?': continue
            elif turn[p[i]][p[i+1]][p[i+2]] != s[i]: ok = 0; break
        ans[0] += ok
    else:
        for i in range(9):
            if not used[i] and (len(p) < 2 or (j:=jump[p[-1]][p[-2]]) == None or used[j]):
                used[i] = 1; p.append(i)
                solve(used, p)
                used[i] = 0; p.pop()
solve(), print(ans[0])