# coding: utf-8

from bintree2 import *

s = "(2 + 3) * 5"

T = makeTree ( s )

KLP( T )
LKP( T )
LPK( T )
BFS( T )

print ( "Результат: ", calcTree ( T ) )


