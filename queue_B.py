
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
    for k in range(D):
      s = x + Q[k]
      if maxSum == None or s > maxSum:
         maxSum = s
    Q.pop(0)

print( maxSum )