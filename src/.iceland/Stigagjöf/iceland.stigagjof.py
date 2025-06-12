m=input();z=0
for _ in range(int(input())):a,b,c=input().split();z=max(z,int(c))if b==m else z
print(z)