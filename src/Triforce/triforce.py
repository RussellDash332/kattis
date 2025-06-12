d=[0,1,4,13]
for _ in'.'*9999:d.append((2*d[-1]+4*d[-2]+2*d[-3])%(10**6+9))
print(d[int(input())])