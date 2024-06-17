input();z=t=d=0
for i in input():d+=(2*t-1)*(i<'1');z+=abs(d);t^=1
print([z,'impossible'][d!=0])