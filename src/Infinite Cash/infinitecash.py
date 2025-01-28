s,d,m=[int(input(),2)for _ in'...']
if d>1000:print(bin(len(bin(m))-2)[2:]),exit(0)
for t in range(5**5):
 if m<1:print(bin(t)[2:]),exit(0)
 m>>=1
 if t%d==d-1:m+=s
print('Infinite money!')