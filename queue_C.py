
Q = []
D = 5

maxSum = None
maxPrev = None
with open( "queue.dat" ) as F:
  N = int( F.readline() )
  for i in range(D):
    Q.append( int(F.readline()) )
  for i in range(N-D):
    x = int( F.readline() )
    if maxPrev != None:
      s = x + maxPrev
      if maxSum == None or s > maxSum:
        maxSum = s
    Q.append( x )
    out = Q.pop(0)
    if maxPrev == None or out > maxPrev:
      maxPrev = out

print( maxSum )