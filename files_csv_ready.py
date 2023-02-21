class TFile:
  name = ''
  size = 0
  typ = ''
  create_date = ''
  mod_date = ''
  access = ''

Files = []
F = open( "files.csv" )
for line in F:
  data = line.rstrip().split(',')
  f = TFile()
  f.name = data[0]
  f.size = int(data[1])
  f.typ = data[2]
  f.create_date = data[3]
  f.mod_date = data[4]
  f.access = data[5]
  Files.append( f )
F.close()

cntAudio = cntVideo = cntImage = cntPpt = cntText = cntXls = 0
for f in Files:
  if "ау" in f.typ: cntAudio += 1
  elif "виде" in f.typ: cntVideo += 1
  elif "изо" in f.typ: cntImage += 1
  elif "през" in f.typ: cntPpt += 1
  elif "текст" in f.typ: cntText += 1
  elif "таб" in f.typ: cntXls += 1

print( "              Аудио:", cntAudio )
print( "              Видео:", cntVideo )
print( "        Изображения:", cntImage )
print( "        Презентации:", cntPpt )
print( "              Текст:", cntText )
print( "Электронные таблицы:", cntXls )

Files.sort( key = lambda f: f.size, reverse = True )
largeFiles = Files[:10]
largeFiles.sort( key = lambda f: f.name )
print( "\nСамые большие файлы: ")
for f in largeFiles:
  print( f.name, f.size)

specFiles = []
for f in Files:
  if "през" in f.typ and "2012" in f.mod_date \
     and "огра" in f.access:
    specFiles.append( f )

print( "\nПрезентации ограниченного доступа (2012): ")
specFiles.sort( key = lambda f: f.name )
for f in specFiles:
  print( f.name, f.typ, f.mod_date, f.access )

specFiles = []
for f in Files:
  if "вид" in f.typ and f.size > 100*1024 and \
     ( "07.2011" in f.create_date or
       "08.2011" in f.create_date or
       "09.2011" in f.create_date or
       "10.2011" in f.create_date or
       "11.2011" in f.create_date or
       "12.2011" in f.create_date
     ):
    specFiles.append( f )

print( "\nВидео > 100 Мбайт (>= 01.07.2011): ")
specFiles.sort( key = lambda f: f.size, reverse = True )
for f in specFiles:
  print( f.name, f.size, f.create_date )





