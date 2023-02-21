s = "([()]{()})"
s = "([()]]{()})"
s = "([()]{()})["

pairs = { "(": ")", "[": "]", "{": "}" }
stack = []
err = False
pos = None
for i, c in enumerate(s):
  if c in pairs:
    stack.append( pairs[c] );
  elif c in pairs.values():
    if not stack or c != stack.pop():
      err = True
      pos = i
      break
if stack: err = True
if not err:
  print("OK")
else:
  print("Not OK")
  print( s )
  print( " "*i + '^' )
