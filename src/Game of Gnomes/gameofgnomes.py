n, m, k = map(int, input().split()); z = 0
for g in range(max(n//k-m, 0), n//k+1): r, s = divmod(n-g*k, m); p = m-s; q = s; z = max(z, g*(g+1)//2*k + ((g+q)*(g+q+1)-g*(g+1))//2*(r+1) + ((g+q+p)*(g+q+p+1)-(g+q)*(g+q+1))//2*r)
print(z)