class TNode:
  data = ""
  left = None
  right = None

def node(d, L = None, R = None):
  n = TNode()
  n.data = d
  n.left = L
  n.right = R
  return n

T = node ( "*",
      node ( "+",
        node ( "1" ),
        node ( "4" )
        ),
      node ( "-",
        node ( "9" ),
        node ( "5" )
        )
      )

def DFS ( T, topLevel = True ):
  if not T: return
  print(T.data, end=" ")
  DFS(T.left, False)
  DFS(T.right, False)
  if topLevel: print()

def DFS_stack ( T, topLevel = True ):
  stack = [T]
  while stack:
    V = stack.pop()
    print(V.data, end=" ")
    if V.right: stack.append(V.right)
    if V.left: stack.append(V.left)
  print()

def LPK ( T, topLevel = True ):
  if not T: return
  LPK(T.left, False)
  LPK(T.right, False)
  print(T.data, end=" ")
  if topLevel: print()

def LKP ( T, topLevel = True ):
  if not T: return
  LKP(T.left, False)
  print(T.data, end=" ")
  LKP(T.right, False)
  if topLevel: print()

def BFS ( T, topLevel = True ):
  queue = [T]
  while queue:
    V = queue.pop(0)
    print(V.data, end=" ")
    if V.left: queue.append(V.left)
    if V.right: queue.append(V.right)
  print()

DFS( T )
DFS_stack( T )
LKP( T )
LPK( T )

BFS( T )