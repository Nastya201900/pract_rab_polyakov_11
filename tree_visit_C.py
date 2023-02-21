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

def readTree( fileName ):
  def makeTree( i ):
    if i >= len(s) or s[i] == '.' : # точка - нет узла
      return None
    P = node( s[i], makeTree(2*i+1),  makeTree(2*i+2) )
    return P
  with open(fileName) as F:
    s = F.readline().split() + ['.'] * 100
  T = makeTree( 0 )
  return T

T = readTree( "tree.dat" )

def BFS ( T, topLevel = True ):
  queue = [T]
  while queue:
    V = queue.pop(0)
    print(V.data, end=" ")
    if V.left: queue.append(V.left)
    if V.right: queue.append(V.right)
  print()

BFS( T )