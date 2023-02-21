# coding: utf-8

def addToTree(s, T, k):
  while k > len(T)-1:
    T.append(None)
  T[k] = s

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

def makeTree ( s, Tree, root = 0 ):
  s = s.strip()
  k = lastOp(s)
  if k < 0:
    if s[0] == '(' and s[-1] == ')':
      makeTree ( s[1:-1], Tree, root )
    else:
      addToTree ( s, Tree, root )
  else:
    addToTree ( s[k], Tree, root )
    makeTree ( s[:k], Tree, 2*root+1 )
    makeTree ( s[k+1:], Tree, 2*root+2 )

def oper( op, n1, n2 ):
  if op == "+":   return n1 + n2
  elif op == "-": return n1 - n2
  elif op == "*": return n1 * n2
  else:           return n1 // n2

def calcTree ( Tree, root = 0 ):
  if 2*root+2 >= len(Tree) or not Tree[2*root+1]:
    return int(Tree[root])
  else:
    n1 = calcTree ( Tree, 2*root+1 )
    n2 = calcTree ( Tree, 2*root+2 )
    return oper(Tree[root], n1, n2)

def KLP ( Tree, root = 0, topLevel = True ):
  if root >= len(Tree): return
  if Tree[root] != None:
    print( Tree[root], end=" ")
  KLP( Tree, 2*root+1, False )
  KLP( Tree, 2*root+2, False )
  if topLevel: print()

def LPK ( Tree, root = 0, topLevel = True ):
  if root >= len(Tree): return
  LPK( Tree, 2*root+1, False)
  LPK( Tree, 2*root+2, False)
  if Tree[root] != None:
    print( Tree[root], end=" " )
  if topLevel: print()

def LKP ( Tree, root = 0, topLevel = True ):
  if root >= len(Tree): return
  LKP( Tree, 2*root+1, False)
  if Tree[root] != None:
    print( Tree[root], end=" " )
  LKP( Tree, 2*root+2, False)
  if topLevel: print()

def BFS ( Tree, topLevel = True ):
  queue = [0]
  while queue:
    root = queue.pop(0)
    if Tree[root] != None:
      print( Tree[root], end=" " )
    if 2*root+1 < len(Tree):
      queue.append( 2*root+1 )
    if 2*root+2 < len(Tree):
      queue.append( 2*root+2 )
  print()

