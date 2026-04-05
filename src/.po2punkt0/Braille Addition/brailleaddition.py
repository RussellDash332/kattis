H=['.***..','*.....','*.*...','**....','**.*..','*..*..','***...','****..','*.**..','.**...']
a=['']*int(input())
for _ in'...':a=[x+y for x,y in zip(a,input().split())]
b=['']*int(input())
for _ in'...':b=[x+y for x,y in zip(b,input().split())]
for i in range(3):print(' '.join(H[int(s)][2*i:2*i+2]for s in str(sum(int(''.join(map(lambda x:str(H.index(x)),y)))for y in(a,b)))))