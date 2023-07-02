import sys
fp = [0, 0.4, 0.9]
def solve(s, p, y, j): # proof by AC?
    min_Y = max(0, (j+12-y-p)//3-4)
    for Y in range(min_Y, min_Y+10):
        for S in range(Y+min(p+s,y)-4, Y+max(p+s,y)+4):
            for P in range(Y+p-4, Y+p+4):
                for oy in fp:
                    for os in fp:
                        for op in fp:
                            yy, ss, pp = Y+oy, S+os, P+op
                            if int(ss-pp)==s and int(pp-yy)==p and int(ss-yy)==y and int(yy)+int(ss)+int(pp)==j+12: return int(ss), int(pp), int(yy)
for l in sys.stdin: print(*solve(*map(int, l.split())))