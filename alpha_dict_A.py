D = {}
F = open ( "listwords.txt" )
while True:
  word  = F.readline().strip()
  if not word:
    break
  D[word] = D.get ( word, 0 ) + 1
F.close()

with open( "listwords.dic", "w" ) as F:
  for w in sorted(D.keys()):
    F.write( w + ": " + str(D[w]) + "\n" )