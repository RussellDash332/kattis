m=[1,2,3,4,5,6,7,9];n=int(input())-1;k=1
while n>=8**k:n-=8**k;k+=1
for r in oct(n)[2:].zfill(k):print(m[int(r)],end='')