from math import *
C = 'N NbE NNE NEbN NE NEbE ENE EbN E EbS ESE SEbE SE SEbS SSE SbE S SbW SSW SWbS SW SWbW WSW WbS W WbN WNW NWbW NW NWbN NNW NbW'.split()
M = {C[i]: (-i+8)%32*pi/16 for i in range(32)}
while (n:=int(input())):
    P = []; x = y = cx = cy = 0; Z = 1e9
    for _ in range(n): d, k = input().split(); k = int(k); P.append((d, k))
    D = float(input())*pi/180; U = [(0, 0)]
    for d, k in P: x += k*cos(M[d]-D); y += k*sin(M[d]-D); cx += k*cos(M[d]); cy += k*sin(M[d]); U.append((cx, cy))
    for i in range(n):
        (x1, y1), (x2, y2) = U[i], U[i+1]
        A, B, C = y2-y1, x1-x2, (y1-y2)*x1+(x2-x1)*y1
        if min((x1-x)*(x1-x2)+(y1-y)*(y1-y2), (x2-x1)*(x2-x)+(y2-y1)*(y2-y)) >= 0: S = abs(A*x+B*y+C)/hypot(A, B)
        else: S = min(hypot(x-x1, y-y1), hypot(x-x2, y-y2))
        Z = min(Z, round(S, 2))
    print('%.2f'%Z)