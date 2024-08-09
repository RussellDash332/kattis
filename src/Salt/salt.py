n = int(input()); a = [*map(int, input().split())]
print(0 if n == 1 else max((a[i]&(v:=a[i-1]^a[i]))^((v+1)//2) for i in range(1, n)))