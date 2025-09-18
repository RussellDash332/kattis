I=__import__('sys').stdin.readline;n,q=map(int,I().split());x={I()for _ in'.'*n}
for _ in'.'*q:print(['why bother?','apply'][all([I()in x for _ in'.'*int(I())])])