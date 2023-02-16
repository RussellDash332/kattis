import sys
input()
ttt = []
configs = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
for line in sys.stdin:
    line = line.strip()
    if not line: ttt.clear()
    else:
        ttt.append(line)
        if len(ttt) == 3:
            p = {'X': set(), 'O': set(), '.': set()}
            for r in range(3):
                for c in range(3):
                    p[ttt[r][c]].add(3*r+c)
            valid, x_win, o_win = False, [False], [False]
            for s, v in ((p['X'], x_win), (p['O'], o_win)):
                for config in configs:
                    if not config - s:
                        v[0] = True
                        break
            if len(p['O']) == len(p['X']):      valid = not x_win[0]
            elif len(p['O'])+1 == len(p['X']):  valid = not o_win[0]
            print('yneos'[1-valid::2])