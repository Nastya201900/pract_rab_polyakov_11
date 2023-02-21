import re, string

punctuation = string.punctuation + "«…»„“–"

D = {}

F = open ( "text.txt" )
allText = F.readlines()
F.close()

for s in allText:
  s = s.strip()
  if s:
    s = re.sub('[%s]' % re.escape(punctuation), '', s)
    words = s.lower().split()
    for w in words:
      D[w] = D.get(w, 0) + 1

wordStat = [ (w,D[w]) for w in D ]
wordStat.sort( key = lambda x: (-x[1], x[0]) )

with open( "listwords.dic", "w" ) as F:
  for word, count in wordStat:
    F.write( word + ": " + str(count) + "\n" )