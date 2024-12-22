n = int(input())
p = [[2*i] for i in range(1, 21)]+[[50]]
for i in [*p]:
    for x in range(1, 21): p.append([x]+i); p.append([2*x]+i); p.append([3*x]+i)
    p.append([25]+i); p.append([50]+i)
for i in [*p]:
    for x in range(1, 21): p.append([x]+i); p.append([2*x]+i); p.append([3*x]+i)
    p.append([25]+i); p.append([50]+i)
for i in p:
    if sum(i)==n:
        for j in range(len(i)-1):
            if i[j]==50: print('bullseye')
            elif i[j]==25: print('single bull')
            elif i[j]%3==0: print('triple', i[j]//3)
            elif i[j]%2==0: print('double', i[j]//2)
            else: print('single', i[j])
        if i[-1] == 50: print('bullseye')
        else: print('double', i[-1]//2)
        exit(0)
print('impossible')