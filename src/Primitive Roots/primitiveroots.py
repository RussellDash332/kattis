from math import gcd
import subprocess
m = int(input())
p = [*map(int, subprocess.check_output(f"factor {m}|cut -d':' -f2",shell=True).split())]
if m in (1, 2, 4) or len({*p}) == 1 or (p.count(2) == 1 and len({*p}) == 2):
    t = m
    for i in {*p}: t = t//i*(i-1)
    q = {*map(int, subprocess.check_output(f"factor {t}|cut -d':' -f2",shell=True).split())}
    for i in range(m):
        if gcd(i, m) == 1 and 1 not in {pow(i, t//j, m) for j in q} and pow(i, t, m) == 1: print(i); exit(0)
print(-1)