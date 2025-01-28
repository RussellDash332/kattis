M=10**9+7;Z=E=0
for _ in'.'*int(input()):a,b=map(int,input().split());Z+=a*b;E+=a+b
print([pow(2,Z-1,M),0][E%2])