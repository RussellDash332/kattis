import sys; input = sys.stdin.readline
T = [(0, 3), (1, 3), (1, 4), (2, 4), (0, 5), (2, 5)]
U = [(5, 0, 4, 1), (3, 1, 5, 2), (4, 2, 3, 0)]
def f(v, i):
    v[T[i][0]] += v[T[i][1]]; v[T[i][1]] = 0; p, q, r, s = U[i//2]
    x = min(v[p], -v[q]%k); v[q] += x; v[3-q-s] += v[p]-x
    y = min(v[6], -v[q]%k); v[q] += y; v[6] -= y
    x = min(v[r], -v[s]%k); v[s] += x; v[3-q-s] += v[r]-x
    y = min(v[6], -v[s]%k); v[s] += y; v[6] -= y
    v[3-q-s] += v[6]; return (v[0]+k-1)//k+(v[1]+k-1)//k+(v[2]+k-1)//k
for _ in range(int(input())): k = int(input()); v = [*map(int, input().split())]; print(min(f([*v], i) for i in range(6)))