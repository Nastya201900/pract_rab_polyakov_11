from bintree_arr import *

s = "2 + 3 * 5"

Tree = []
makeTree ( s, Tree )

KLP( Tree )
LKP( Tree )
LPK( Tree )
BFS( Tree )

print ( "Результат: ", calcTree ( Tree ) )


