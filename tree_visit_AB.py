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

def DFS ( T ):
  if not T: return
  print(T.data, end=" ")
  DFS(T.left)
  DFS(T.right)

def DFS_stack ( T ):
  stack = [T]
  while stack:
    V = stack.pop()
    print(V.data, end=" ")
    if V.right: stack.append(V.right)
    if V.left: stack.append(V.left)

def LPK ( T ):
  if not T: return
  LPK(T.left)
  LPK(T.right)
  print(T.data, end=" ")
def LKP ( T ):
  if not T: return
  LKP(T.left)
  print(T.data, end=" ")
  LKP(T.right)

def BFS ( T ):
  queue = [T]
  while queue:
    V = queue.pop(0)
    print(V.data, end=" ")
    if V.left: queue.append(V.left)
    if V.right: queue.append(V.right)

DFS( T ); print()
DFS_stack( T ); print()
LKP( T ); print()
LPK( T ); print()

BFS( T ); print()