n, m = map(int, input().split())
if n%5 and m%5: print('no'), exit(0)
if n==1 and m!=5: print('no'), exit(0)
if m==1 and n!=5: print('no'), exit(0)
if n==2 and m==5: print('no'), exit(0)
if m==2 and n==5: print('no'), exit(0)
if n==1 and m==5: print('yes\nIIIII'), exit(0)
if n==5 and m==1: print('yes\nI\nI\nI\nI\nI'), exit(0)
if n==2 or m==2:
    print('yes'); sw = m==2
    if sw: n, m = m, n
    Z = ['LLLLNNNPPP'*(m//10) if m%2==0 else 'PPPYNNNYYYYNNPP'+'LLLLNNNPPP'*((m-15)//10), 'LIIIIINNPP'*(m//10) if m%2==0 else 'PPYYYYNNYNNNPPP'+'LIIIIINNPP'*((m-15)//10)]
    if sw: print('\n'.join(''.join(z) for z in zip(*Z)))
    else: print('\n'.join(''.join(z) for z in Z))
    exit(0)
a3 = ['UUXUU', 'UXXXU', 'UUXUU']; b3 = ['PPTPP', 'PPTPP', 'PTTTP']
a4 = ['LPPPY', 'LWPPY', 'LWWYY', 'LLWWY']
a5 = a4+['IIIII']; b5 = ['IIIII']+a4
sw = m%5 != 0; print('yes')
if sw: n, m = m, n
Z = [['?']*m for _ in range(n)]; T = ((), (a4,), (a5, b5))
for i in range((n-(0, 4, 5)[n%3])//3):
    for j in range(m//5):
        for k in range(3):
            for l in range(5): Z[3*i+k][5*j+l] = (a3, b3)[(i+j)%2][k][l]
for i in range((0, 4, 5)[n%3]):
    for j in range(m//5):
        for l in range(5): Z[n-(0, 4, 5)[n%3]+i][5*j+l] = T[n%3][j%len(T[n%3])][i][l]
if sw: print('\n'.join(''.join(z) for z in zip(*Z)))
else: print('\n'.join(''.join(z) for z in Z))