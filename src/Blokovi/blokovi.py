N,*M=map(int,open(0));S=M.pop();D=1
while len(M)-1:m=M.pop();S+=m;D=max(max(D,2)-m/S,D+m/S)
print(D)