n,g,*a=map(int,open(0).read().split());g-=10;z={1}
for i in sorted(a):z|={j+67*i+1for j in z};z={j for j in z if j//67-g<=j%67*5}
print(max([(j//67-g)/(j%67)for j in z if j>=67*g]or['impossible']))