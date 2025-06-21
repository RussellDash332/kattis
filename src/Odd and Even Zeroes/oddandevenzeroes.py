X = [1]
for _ in range(15): X.append(2*25**(_+1)//5+5*X[-1])
while (n:=int(input())) != -1:
    z = p = 0; n += 1
    for i in range(15, -1, -1):
        for j in range(n//25**i):
            if p^(j%10<5): z += X[i]
            else: z += 25**i-X[i]
        p ^= (n//25**i)%10>4; n %= 25**i
    print(z)