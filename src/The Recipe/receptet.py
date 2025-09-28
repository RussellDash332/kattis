for s in[*open(z:=0)][1:]:a,b,c=map(int,s.split());z+=max(b-a,0)*c
print(z)