A, B, M = map(int, input().split())
d = [Z:=0]*B; r = d[0] = 1
for i in range(A-1):
    q = 0
    for j in range(B): u = (s:=i+j+2)*(q+d[j])%M; d[j] = (q+s*d[j])%M; q = u
for j in range(B)[::-1]: Z = (Z+d[j]*r)%M; r= r*(A+j)%M
print(Z)