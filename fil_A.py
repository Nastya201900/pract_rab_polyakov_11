
A = [
[0,	1,	0,	1,	1],
[1,	1,	1,	2,	2],
[0,	1,	0,	2,	2],
[3,	3,	1,	2,	2],
[0,	1,	1,	0,	0]
 ]
 
NEW_COLOR = 2 
YMAX = len(A)
XMAX = len(A[0])
(x0,y0) = (1,0)
color = A[y0][x0]
Q = []
Q.append ( (x0,y0) )
print(Q)

while Q:
  x, y = Q.pop(0)
  if A[y][x] == color:
    A[y][x] = NEW_COLOR
    if x > 0: Q.append( (x-1,y) )
    if x < XMAX-1: Q.append( (x+1,y) )
    if y > 0: Q.append( (x,y-1) )
    if y < YMAX-1: Q.append( (x,y+1) )

for row in A:
  for x in row:
    print( "{:4d}".format(x), sep="", end="")
  print()