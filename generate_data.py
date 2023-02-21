from random import randint

N = 1000

with open( "queue.dat", "w" ) as F:
  F.write( str(N) + "\n" )
  for i in range(N):
    F.write( str(randint(-999, 1000)) + "\n" )