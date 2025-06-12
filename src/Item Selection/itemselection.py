n, m, s, p, q = map(int, input().split()); s -= 1; S = []
A = [set() for _ in range((n+m-1)//m)]
B = [set() for _ in range((n+m-1)//m)]
for _ in range(p): x = int(input())-1; A[x//m].add(x)
for _ in range(q): x = int(input())-1; B[x//m].add(x)
for i in range((n+m-1)//m):
    a, b = A[i], B[i]
    z = len(a^b) # deselect 1b1 then select 1b1
    z = min(z, len(b)+1) # deselect all then select 1b1
    z = min(z, min(n, (i+1)*m)-i*m-len(b)+1) # select all then deselect 1b1
    if len(b) == min(n, (i+1)*m)-i*m or len(b) == 0: z = min(z, 1) # just (de)select all
    S.append(z)
l = 0; r = len(S)-1
while l < len(S) and S[l] == 0: l += 1
while r > -1 and S[r] == 0: r -= 1
if r == -1: print(0)
else: print(min(abs(r-s),abs(s-l))+r-l+sum(S))