from heapq import*;P=heappop;N,D,L,*A=map(int,open(0).read().split());heapify(A);P(A)
while A:heappush(A,P(A)+D);M=P(A)+L
print(M)