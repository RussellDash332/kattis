M=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];a,b,c=map(M.index,[input()for _ in'...'])
for a,b,c in((a,b,c),(a,c,b),(b,c,a),(b,a,c),(c,a,b),(c,b,a)):
 if(b-a)%12==4==(c-b)%12+1:print(M[a],'major')>exit()
print('not a chord')