# coding: utf-8

from bintree_arr2 import *

s = "(2 + 3) * 5"

Tree = []
makeTree ( s, Tree )

KLP( Tree )
LKP( Tree )
LPK( Tree )
BFS( Tree )

print ( "Результат: ", calcTree ( Tree ) )
