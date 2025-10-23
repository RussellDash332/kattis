from base64 import*;s=[*map(int,b64decode(input()))];a,b,c=[s[i+1]%12for i in range(len(s))if s[i]==144]
for a,b,c in((a,b,c),(a,c,b),(b,c,a),(b,a,c),(c,a,b),(c,b,a)):
 if(b-a)%12==4==(c-b+1)%12:print(['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][a],'major')>exit()
print('not a chord')