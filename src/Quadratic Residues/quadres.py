for _ in'.'*int(input()):a,p=map(int,input().split());print('yneos'[(pow(a,(p-1)//2,p)==p-1)*(a%p>0)::2])