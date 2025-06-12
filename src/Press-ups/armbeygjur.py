import subprocess
n = 2*int(input()); e = 1; v = {1}; z = set()
while n%e==0: e *= 2
for i in map(int, subprocess.check_output(f"factor {2*n//e}|cut -d':' -f2",shell=True).split()): v = v|{x*i for x in v}
for i in v: z.add(((n//i-i+1)//2, i)); z.add(((i-n//i+1)//2, n//i))
for f, d in sorted(z): f > 0 and print(f, d)