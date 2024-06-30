N, K, M = map(int, input().split()); M = 1<<M; A = [0]*M; Z = 0; I = pow(33, -1, M); P = M-1
if N > 1:
 for a in range(1, 27):
  if N < 4: A[a] += 1; continue
  for b in range(1, 27):
   h = ((33*a)^b)&P
   if N < 6: A[h] += 1; continue
   for c in range(1, 27):
    h2 = ((33*h)^c)&P
    if N < 8: A[h2] += 1; continue
    for d in range(1, 27):
     h3 = ((33*h2)^d)&P
     if N < 10: A[h3] += 1; continue
     for e in range(1, 27): A[((33*h3)^e)&P] += 1
else: A[0] += 1
for a in range(1, 27):
 h = (K^a)*I&P
 if N < 3: Z += A[h]; continue
 for b in range(1, 27):
  h2 = (h^b)*I&P
  if N < 5: Z += A[h2]; continue
  for c in range(1, 27):
   h3 = (h2^c)*I&P
   if N < 7: Z += A[h3]; continue
   for d in range(1, 27):
    h4 = (h3^d)*I&P
    if N < 9: Z += A[h4]; continue
    for e in range(1, 27): Z += A[(h4^e)*I&P]
print(Z)