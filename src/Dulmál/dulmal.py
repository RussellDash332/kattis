from math import gcd
import subprocess
m, n = map(int, input().split()); m += 1
if m < 1000: print('OGg'[len({pow(n,x,m)for x in range(2*m)})==m-1::2]+'ild leynitala!'); exit()
p = [*map(int, subprocess.check_output(f"factor {m}",shell=1).split()[1:])]
if m in (1, 2, 4) or len({*p}) == 1 or (p.count(2) == 1 and len({*p}) == 2):
    t = m
    for i in {*p}: t = t//i*(i-1)
    q = {*map(int, subprocess.check_output(f"factor {t}",shell=1).split()[1:])}
    if gcd(n, m) == 1 and 1 not in {pow(n, t//j, m) for j in q} and pow(n, t, m) == 1: print('Gild leynitala!'); exit()
print('Ogild leynitala!')