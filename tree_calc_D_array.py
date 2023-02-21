# coding: utf-8

from bintree_arr3 import *

s = "2 * * 5"

def showTree( Tree, root = 0, level = 0 ):
  if root >= len(Tree): return
  print( "  "*level + str(Tree[root]) )
  showTree( Tree, 2*root+1, level + 1 )
  showTree( Tree, 2*root+2, level + 1 )

Tree = []
makeTree ( s, Tree )

showTree( Tree )

KLP( Tree )
LKP( Tree )
LPK( Tree )
BFS( Tree )

res = calcTree ( Tree )
if res == None:
  print ( "Неверное выражение" )
else:
  print ( "Результат: ", res )
