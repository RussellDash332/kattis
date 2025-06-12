import sys; input = sys.stdin.readline
N = int(input()); P = []
for _ in range(N): t, v = map(int, input().split()); P.append((t, v))
def f(n): p = [max((n-t)*v, 0) for t, v in P]; return max(p)-min(p)
a, b = max(P)[0], 10**9; gr = (5**0.5-1)/2; tol = 1e-6
while b-a>tol:
    if f(μ:=(1-gr)*a+gr*b) > f(λ:=gr*a+(1-gr)*b): b = μ
    else: a = λ
print(int(f((a+b)/2)*1000)/1000-8e-3)