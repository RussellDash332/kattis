import sys
F = [1, 1]; T = 0
for _ in range(100): F.append(F[-2]+F[-1])
def c(s): return s.replace('10', '@').replace('1', '0').replace('@', '1')
def f(p, n):
    if n < 2: return int(str(n)==p)
    if '00' in p or len(p) > F[n]: return 0
    if len(p) == 1: return F[n-2+int(p)]
    if p[0] == '0': return f('1'+p, n)
    return (f(c(p+'0'), n-1) if p[-1]=='1' else 0)+f(c(p), n-1)
for l in sys.stdin: T += 1; print(f'Case {T}: {f(sys.stdin.readline().strip(), int(l))}')