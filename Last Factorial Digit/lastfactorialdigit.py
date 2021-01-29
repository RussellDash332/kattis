q = int(input())
for _ in range(q):
    n = int(input())
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact%10)