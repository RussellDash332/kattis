n = int(input())
for _ in range(n):
    i,p = map(int,input().split(" "))
    print(f"{i} {p*(p+1)//2} {p**2} {p*(p+1)}")