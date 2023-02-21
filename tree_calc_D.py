# coding: utf-8

from bintree3 import *

def showTree( T, level = 0 ):
  if not T: return
  print( "  "*level + str(T.data) )
  showTree( T.left, level + 1)
  showTree( T.right, level + 1)

s = "2 ** 5"

T = makeTree ( s )

showTree( T )

KLP( T )
LKP( T )
LPK( T )
BFS( T )

res = calcTree ( T )
if res == None:
  print ( "Неверное выражение" )
else:
  print ( "Результат: ", res )


