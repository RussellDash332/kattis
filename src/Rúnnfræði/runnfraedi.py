A, a = input().split('.')
B, b = input().split('.')
M = max(len(A), len(B)); A = [0]*(M-len(A))+[*map(int, A)]; B = [0]*(M-len(B))+[*map(int, B)]
m = max(len(a), len(b)); a = [*map(int, a)]+[0]*(m-len(a)); b = [*map(int, b)]+[0]*(m-len(b))
X = A+a; Y = B+b
for i in range(M+m):
    if X[i] != Y[i]:
        x = int(''.join(map(str, X[max(i-2,0):i+2]))); y = int(''.join(map(str, Y[max(i-2,0):i+2]))); Z = 0
        for i in range(1, 5): d = x//10**(i-1)%10; t = x//10**i*10**i; r = t+10**i*(d>4); Z |= (r==y)|(2*(t==y))
        print(['Runnun', 'Styfun', 'Veit ekki'][Z-1]), exit()