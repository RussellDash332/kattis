K, q = map(int, input().split())
if K == 2:
    def do(i): print(*(int(i==j) for j in range(q))); return int(input())
    print(*(do(i) for i in range(q)))
elif K == 4:
    def do(i): print(*((100, 1)[j%2]*(i==j//2) for j in range(2*q))); return divmod(int(input()), 100)
    print(*sum((do(i) for i in range(q)), ()))
elif K == 3:
    def do(i): print(*((100, 1, 0)[j%3]*(i==j//3) for j in range(3*q//2))); a, Bb = divmod(int(input()), 100); print(*((10, 0, 1)[j%3]*(i==j//3) for j in range(3*q//2))); A, Cc = divmod(int(input())-10*a, 100); return (10*A+a)%100, Bb, Cc
    print(*sum((do(i) for i in range(q//2)), ()))