M=[20,1,18,4,13,6,10,15,2,17,3,19,7,16,8,11,14,9,12,5]
for _ in[*open(0)][1:]:a,b,c=sorted(map(M.index,map(int,_.split())));print(max(sum(M[a:b+1]),sum(M[b:c+1]),sum(M[c:]+M[:a+1])if c>a else M[a]))