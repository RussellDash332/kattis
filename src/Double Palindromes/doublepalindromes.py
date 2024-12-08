n=int(input());z=1
for i in range(1,10**6):
 for d in(0,1):s=str(i);b=int(s[:len(s)-d]+s[::-1]);c=bin(b)[2:];z+=b<n!=c==c[::-1]
print(z)