b = [input() for _ in range(8)]
for i in range(8):
    for j in range(8):
        if b[i][j] == 'K': wkr, wkc = i, j
        if b[i][j] == 'R': wrr, wrc = i, j
        if b[i][j] == 'k': bkr, bkc = i, j
s = []
cr = wrr-1
while cr>=0 and b[cr][wrc] == '.': s.append((cr, wrc)); cr -= 1
cr = wrr+1
while cr<8 and b[cr][wrc] == '.': s.append((cr, wrc)); cr += 1
cc = wrc-1
while cc>=0 and b[wrr][cc] == '.': s.append((wrr, cc)); cc -= 1
cc = wrc+1
while cc<8 and b[wrr][cc] == '.': s.append((wrr, cc)); cc += 1

for rr, rc in s:
    hit = pos = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if 0<=bkr+dr<8 and 0<=bkc+dc<8:
                tr, tc = bkr+dr, bkc+dc
                pos += 1; safe = True
                for ddr in range(-1, 2):
                    for ddc in range(-1, 2):
                        if (ddr or ddc) and (tr+ddr, tc+ddc) == (wkr, wkc): safe = False
                        if not safe: break
                    if not safe: break
                safe *= 1-(tr == rr)^(tc == rc)
                hit += 1-safe
    if hit == pos: print('Yes'), exit(0)
print('No')