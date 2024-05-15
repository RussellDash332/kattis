import sys; input = sys.stdin.readline; from datetime import *
for _ in range(int(input())):
    B, C = map(int, input().split()); Q = []; a = c = 0
    for _ in range(B): _, sd, st, ed, et = input().split(); s = datetime.strptime(sd+' '+st, '%Y-%m-%d %H:%M'); e = datetime.strptime(ed+' '+et, '%Y-%m-%d %H:%M')+timedelta(minutes=C); Q.append((s, 1)); Q.append((e, -1))
    for x, v in sorted(Q): c += v; a = max(a, c)
    print(a)