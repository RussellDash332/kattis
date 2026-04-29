n=int(input());l=h=0
for c in input():l,h=[(max(0,l+1-(c>'(')*2),h+1-(c==')')*2),(1,h)][h<0]
print("YNEOS"[n%2or l>0::2])