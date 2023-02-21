
with open("fill.dat") as F:
  N, M = map( int, F.readline().split() )
  A = []
  for i in range(N):
    row = list(map(int, F.readline().split()))
    A.append( row )

def printMatrix( header, A ):
  if header:
    print( header )
  for row in A:
    for x in row:
      print( "{:4d}".format(x), sep="", end="")
    print()

printMatrix( "Исходная матрица",  A )

NEW_COLOR = 2
YMAX = len(A)
XMAX = len(A[0])
(x0,y0) = (1,0)
color = A[y0][x0]
Q = []
Q.append ( (x0,y0) )

print( "Начальная точка", *Q )

def addToQueue( x, y ):
  if A[y][x] != color or (x,y) in Q: return
  if 0 <= x < XMAX and 0 <= y < YMAX:
    Q.append( (x, y) )

step = 0
while Q:
  x, y = Q.pop(0)
  A[y][x] = NEW_COLOR
  addToQueue( x-1, y )
  addToQueue( x+1, y )
  addToQueue( x, y-1 )
  addToQueue( x, y+1 )
  step += 1
  print( "Шаг "+str(step)+" Q =", Q )
  printMatrix( "", A )

printMatrix( "После заливки",  A )
