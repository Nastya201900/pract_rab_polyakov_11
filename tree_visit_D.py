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

def BFS_no_queue ( T ):
  def showTreeLevel( T, level ):
    if not T: return
    if level == 0:
      print( T.data, end = " ")
      return 1
    count = 0
    if T.left:
      count += showTreeLevel( T.left, level-1 )
    if T.right:
      count += showTreeLevel( T.right, level-1 )
    return count
  #-----------------------------------------
  level = 0
  while showTreeLevel( T, level ) > 0:
    level += 1
  print()

BFS_no_queue( T )