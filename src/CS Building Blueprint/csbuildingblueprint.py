import cmath;a,b,c,d,e,f,g,h=map(int,open(0).read().split());P=[complex(i,j)for i,j in zip((a,c,e,g),(b,d,f,h))];P=sorted(P,key=lambda x:cmath.phase(x-sum(P)/4));R=range(4);a,b,c,d=[abs(P[i]-P[i-1])for i in R];L={a,b,c,d};Z=print
if{((P[i]-P[i-1])*(P[i-2]-P[i-1]).conjugate()).real for i in R}=={0}:Z(['Square','Rectangle'][len(L)-1])
elif len(L)<2:Z('Rhombus')
elif(a==c)*(b==d):Z('Parallelogram')
elif(a==b)*(c==d)+(a==d)*(b==c):Z('Kite')
else:N=[(P[i]-P[i-1])/abs(P[i]-P[i-1])for i in R];Z(['Quadrilateral','Trapezoid'][any(abs(a+b)<1e-9for a in N for b in N)])