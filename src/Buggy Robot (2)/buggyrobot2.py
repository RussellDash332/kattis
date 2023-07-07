from collections import deque
R, C = map(int, input().split())
delta = {
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
    'R': (0, 1)
}
m = [list(input().strip()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if m[i][j] == 'R': s = i*C+j
        if m[i][j] == 'E': g = i*C+j
cmd = input().strip()
q, vis = deque([(s, 0, 0)]), set()
while q:
    u, k, fix = q.popleft()
    if u == g: print(fix), exit(0)
    state = 51*u+k
    if state not in vis:
        vis.add(state)
        r, c = u//C, u%C
        if k < len(cmd):
            dr, dc = delta[cmd[k]]
            ok = 0<=r+dr<R and 0<=c+dc<C and m[r+dr][c+dc]!='#'
            q.appendleft(((r+dr*ok)*C+c+dc*ok, k+1, fix))   # obey and move on, prioritize this
            if ok: q.append((u, k+1, fix+1))                # ignore a command, no need to add if initial command is a boundary hit
        for d in delta.values():
            dr, dc = d
            if 0<=r+dr<R and 0<=c+dc<C and m[r+dr][c+dc]!='#': q.append(((r+dr)*C+c+dc, k, fix+1)) # prepend an extra step that doesn't hit anything