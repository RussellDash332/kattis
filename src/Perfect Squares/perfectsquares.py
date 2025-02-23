import subprocess
def find(n, x, m):
    for i in range(n): j = n-i*i; (k:=round(j**.5))**2 == j and print(i*m, k*m, x*m) != exit()
n = int(input()); f = 1
while n%4 == 0: n //= 4; f *= 2
if n%8 == 7: print(-1); exit()
for i in range(n):
    z = n-i*i; m = 1
    while z%2 == 0: z //= 2; m *= 2
    if all(k%4==1 for k in map(int, subprocess.check_output(f"factor {z}|cut -d':' -f2",shell=True).split())): find(z*m, i, f)