
Q = []
D = 5

maxSum = None
with open( "queue.dat" ) as F:
  N = int( F.readline() )
  for i in range(D):
    Q.append( int(F.readline()) )
  for i in range(N-D):
    x = int( F.readline() )
    Q.append( x )
    s = x + Q.pop(0)
    if maxSum == None or s > maxSum:
       maxSum = s

print( maxSum )