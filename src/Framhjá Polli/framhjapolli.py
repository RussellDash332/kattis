from cmath import *
x1, y1, x2, y2, xr, yr, rr = map(eval, open(0).read().split())
p1 = x1+y1*1j; p2 = x2+y2*1j; pr = xr+yr*1j; a1 = acos(rr/abs(d1:=p1-pr)); a2 = acos(rr/abs(d2:=p2-pr))
if abs(((p2-p1)*d1.conjugate()).imag)/abs(p2-p1) >= rr or (d1*(p1-p2).conjugate()).real <= 0 or (d2*(p2-p1).conjugate()).real <= 0: print(abs(p2-p1))
else: print(min(abs(a-p1)+min(k:=(phase(a-pr)-phase(b-pr))%(2*pi), 2*pi-k)*rr+abs(b-p2) for a in [pr+rr*d1/abs(d1)*exp(a1*1j), pr+rr*d1/abs(d1)*exp(a1*-1j)] for b in [pr+rr*d2/abs(d2)*exp(a2*1j), pr+rr*d2/abs(d2)*exp(a2*-1j)]))