D = {}
F = open ( "listwords.txt" )
while True:
  word  = F.readline().strip()
  if not word:
    break
  D[word] = D.get ( word, 0 ) + 1
F.close()

wordStat = [ (w,D[w]) for w in D ]
wordStat.sort( key = lambda x: (-x[1], x[0]) )

with open( "listwords.dic", "w" ) as F:
  for word, count in wordStat:
    F.write( word + ": " + str(count) + "\n" )