A = -1; P = int(input()); n1, n5, n10, n25 = map(int, input().split())
for i in range(max(n1-24, 0), n1+1):
    for j in range(max(n5-4, 0), n5+1):
        for k in range(max(n10-4, 0), n10+1):
            l = P-i-5*j-10*k
            if l%25==0 and 0<=l//25<=n25: A = max(A, i+j+k+l//25)
print('Impossible' if A == -1 else A)