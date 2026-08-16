B={1<<i for i in range(67)}
n=int(input())-1
if n<1 or n in B:print(1);exit()
for a in B:
 if n-a in B:print(a+1);exit()
print('impossible')