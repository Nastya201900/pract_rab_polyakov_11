class TNode:
  data = ""
  left = None
  right = None

def newNode(d):
  node = TNode()
  node.data = d
  node.left = None;
  node.right = None
  return node

def priority(op):
  if op in "+-": return 1
  if op in "*/": return 2
  return 100

def lastOp(s):
  minPrt = 50
  nest = 0
  k = -1
  for i in range(len(s)):
    if s[i] == '(': nest += 1
    elif s[i] == ')': nest -= 1
    elif nest == 0  and priority(s[i]) <= minPrt:
      minPrt = priority(s[i])
      k = i
  return k

def makeTree ( s ):
  s = s.strip()
  k = lastOp(s)
  if k < 0:
    if s[0] == '(' and s[-1] == ')':
      Tree = makeTree( s[1:-1] )
    else:
      Tree = newNode ( s )
  else:
    Tree = newNode ( s[k] )
    Tree.left = makeTree ( s[:k] )
    Tree.right = makeTree ( s[k+1:] )
  return Tree

def calcTree ( Tree ):
  if Tree.left == None:
    return int(Tree.data)
  else:
    n1 = calcTree ( Tree.left )
    n2 = calcTree ( Tree.right )
    if Tree.data == "+":   res = n1 + n2
    elif Tree.data == "-": res = n1 - n2
    elif Tree.data == "*": res = n1 * n2
    else: res = n1 // n2
    return res

def KLP ( T, topLevel = True ):
  if not T: return
  print(T.data, end=" ")
  KLP(T.left, False)
  KLP(T.right, False)
  if topLevel: print()

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

