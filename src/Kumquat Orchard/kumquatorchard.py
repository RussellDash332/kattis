N = int(input()); U = 1067
P = [0]*4; Q = 0
for _ in range(N):
    x, y = map(int, input().split())
    if x>0<y: P[0] |= 1
    elif x<0<y: P[1] |= 1
    elif x<0>y: P[2] |= 1
    elif x>0>y: P[3] |= 1
    elif x>0: Q |= 1
    elif y>0: Q |= 2
    else: Q |= 1<<2+(y<0)
Z = lambda x, y, X, Y: f'%.1f %.1f %.1f %.1f %.1f %.1f %.1f %.1f'%(x, y, x, Y, X, Y, X, y)
T, B, L, R, BR, TR, BL, TL = Z(-U, 0.3, U, U), Z(-U, -0.3, U, -U), Z(-U, -U, -0.3, U), Z(U, -U, 0.3, U), Z(0.1, 0.1, U, -U), Z(0.1, -0.1, U, U), Z(-0.1, 0.1, -U, -U), Z(-0.1, -0.1, -U, U)
O = [[*([B] if P[0]==P[1]<1 else [R] if P[1]==P[2]<1 else [T] if P[2]==P[3]<1 else [L] if P[3]==P[0]<1 else [T, B])], [R]+[L]*(P[1]|P[2]), [T]+[B]*(P[2]|P[3]), [T, BR]+[BL]*P[2], [L]+[R]*(P[3]|P[0]), [L, R], [T, BL]+[BR]*P[3], [T, BL, BR], [B]+[T]*(P[0]|P[1]), [B, TR]+[TL]*P[1], [T, B], [R, Z(0.2, 0.2, -U, U), Z(0.2, -0.2, -U, -U)], [B, TL]+[TR]*P[0], [B, TL, TR], [L, Z(-0.2, 0.2, U, U), Z(-0.2, -0.2, U, -U)], [Z(-U, U, U, 0.5), Z(-U, -U, U, -0.5), Z(-U, -0.4, -0.1, 0.4), Z(U, -0.4, 0.1, 0.4)]][Q]
print(len(O), *O)