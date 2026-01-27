a,b=map(int,input().split());S=set()
for x in range(a):
 z=(a-1)**2-x*x
 if z==(y:=round(z**.5))**2and y*~-b%~-a==x*~-b%~-a==0:S.add((x,-y));S.add((x,y))if x else 0
print(len(S)//(1+(a==b)))