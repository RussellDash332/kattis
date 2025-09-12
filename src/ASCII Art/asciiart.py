s=input().strip()
while s!=(s:=s.replace('  ',' ')):1
print({'What is problem A about?':'''Problem A is about Ascii Art
   _     __   __  _   _
  / \   / /  / / | | | |
 / _ \  \ \ | |  | | | |
/_/ \_\ /_/  \_\ |_| |_|''','What is problem B about?':'''Problem B is about Fortnite
###############
###############
####       /###
####   ########
####       ####
####   ########
####   ########
####   ########
####_~<########
###############''','What is problem C about?':'''Problem C is about The Legend of Zelda
     /\\
    /  \\
   /____\\
  /\\    /\\
 /  \\  /  \\
/____\\/____\\'''}.get(s,'I am not sure how to answer that.'))