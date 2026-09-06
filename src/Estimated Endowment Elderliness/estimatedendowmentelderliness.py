N, R = map(eval, input().replace('%', '/100').split()); Z = [1]
for _ in range(N):
    r = float(input()[:-1])/100
    Z += [Z[-1]*(1+r)]
T = Z[-1]/(1+R)
for i in range(N):
    if min(Z[i], Z[i+1]) <= T <= max(Z[i], Z[i+1]): y, m = divmod(N-i, 12); print(f'{y} year{"s"*(y!=1)} and {m} month{"s"*(m!=1)} ago'); exit()
print('something fishy is going on')