
#s = input().split()
s = "5 15 + 4 7 + 1 - /"

data = s.split()
stack = []
err = False
for x in data:
  if x in "+-*/":	# если операция
    if len(stack) < 2:
      err = True
      break
    try:
      op2 = int(stack.pop())
      op1 = int(stack.pop())
    except:
      err = True
      break
    if   x == "+": res = op1 + op2
    elif x == "-": res = op1 - op2
    elif x == "*": res = op1 * op2
    else:         res = op1 // op2
    stack.append ( res )
  else:
    stack.append ( x )
  print( stack )

if len(stack) != 1:
  err = True
elif not err:
  try:
    result = int(stack[0])
  except:
    err = True

if err:
  print( "Неверное выражение", s )
else:
  print ( "Результат:", result )