s = "([()]{()})"

pairs = { "(": ")", "[": "]", "{": "}" }
stack = []
err = False
for c in s:
  if c in pairs:
    stack.append( pairs[c] );
  elif c in pairs.values():
    if not stack or c != stack.pop():
      err = True
      break
if stack: err = True
if not err:
  print("OK")
else:
  print("Not OK")
