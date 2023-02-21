class TPupil:
  fam = ''
  name = ''
    # отметки
  alg = 0
  rus = 0
  fiz = 0
  ist = 0

Pupils = []
F = open( "marks.csv" )
for line in F:
  p = TPupil()
  data = line.rstrip().split(',')
  p.fam = data[0]
  p.name = data[1]
  p.alg = int(data[2])
  p.rus = int(data[3])
  p.fiz = int(data[4])
  p.ist = int(data[5])
  Pupils.append( p )
F.close()

N = len( Pupils )
sumAlg = sumRus = sumFiz = sumIst = 0
for p in Pupils:
  sumAlg += p.alg
  sumRus += p.rus
  sumFiz += p.fiz
  sumIst += p.ist

print( "Средние баллы:" )
print( "Алгебра:      ", sumAlg/N )
print( "Русский язык: ", sumRus/N )
print( "Физика:       ", sumFiz/N )
print( "История:      ", sumIst/N )

maxSum = 0
for p in Pupils:
  s = p.alg + p.rus + p.fiz + p.ist
  maxSum = max( maxSum, s )

print( "\nМаксимальный балл:", maxSum )

Pupils.sort( key = lambda x: x.fam )
for p in Pupils:
  s = p.alg + p.rus + p.fiz + p.ist
  if s == maxSum:
    print( p.fam, p.name )

cnt2 = 0
for p in Pupils:
  if 2 in [p.alg, p.rus, p.fiz, p.ist]:
    cnt2 += 1

print( "\nПолучили 2:", cnt2, "человек" )


