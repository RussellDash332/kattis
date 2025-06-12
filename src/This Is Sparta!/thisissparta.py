import sys; input = sys.stdin.readline
N, K = map(int, input().split()); V = sorted(map(int, input().split()))
def Z():
    if K == 0 or len(V) < 2: print(*([0]*(N-len(V))+V)); exit()
    V.sort()
while K and len(V) > 3:
    K -= 1
    for i in range(1, len(V)): V[i] -= V[i-1]
    Z(); V = [i for i in V if i]
while K and len(V) == 3: k = min(V[1]//V[0], V[2]//V[1], K); K -= k; V = [V[0], V[1]-k*V[0], V[2]-k*V[1]+k*(k+1)//2*V[0]]; Z(); V = [i for i in V if i]
while K and len(V) == 2: k = min(V[1]//V[0], K); K -= k; V = [V[0], V[1]-k*V[0]]; Z(); V = [i for i in V if i]; Z()
Z()