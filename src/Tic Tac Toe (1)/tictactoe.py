import sys

n, m = map(int, input().split())

if n == m == 1: # corner case
    s = input().strip()
    print({
        'X': 'X WINS',
        'O': 'ERROR',
        '.': 'IN PROGRESS'
    }[s])
    sys.exit(0)

ttt = tuple(sys.stdin)
p = {'X': set(), 'O': set(), '.': set()}
for r in range(n):
    for c in range(n):
        p[ttt[r][c]].add(n*r+c)
valid, x_win, o_win = False, [0], [0]
x_ttt, o_ttt = [0]*(n**2), [0]*(n**2)

def check(config, s, v, t):
    if not config - s:
        v[0] += 1
        for i in config: t[i] += 1

for s, v, t in ((p['X'], x_win, x_ttt), (p['O'], o_win, o_ttt)):
    for i in range(n): # horizontal
        for j in range(n-m+1):
            check(set(range(i*n+j, i*n+m+j)), s, v, t)
    for i in range(m): # vertical
        for j in range(n-m+1):
            check(set(range(j*n+i, (j+m)*n+i, n)), s, v, t)
    for i in range(n-m+1): # diagonal
        for j in range(n-m+1):
            check(set(range(i*n+j, (i+m)*n+j, n+1)), s, v, t)
            check(set(range((i+1)*n+j-1, (i+m)*n+j-1, n-1)), s, v, t)

if len(p['O']) == len(p['X']):      valid, candidate = not x_win[0], (o_ttt, o_win, 'O')
elif len(p['O'])+1 == len(p['X']):  valid, candidate = not o_win[0], (x_ttt, x_win, 'X')
else:                               valid, candidate = False, None

if not valid:
    print('ERROR')
elif not candidate[1][0]:
    print('IN PROGRESS' if p['.'] else 'DRAW')
else:
    # one of the tiles must be the result of all the wins, otherwise two independent wins
    t, w, ply = candidate
    print(['ERROR', f'{ply} WINS'][int(w[0] in t)])