
#data = input().split()
data = "/ + 5 15 - + 4 7 1". split()

stack = []
for x in reversed(data):
  if x in "+-*/":	# если операция
    op1 = int(stack.pop())
    op2 = int(stack.pop())
    if   x == "+": res = op1 + op2
    elif x == "-": res = op1 - op2
    elif x == "*": res = op1 * op2
    else:         res = op1 // op2
    stack.append ( res )
  else:
    stack.append ( x )
  print( stack )

print ( "Результат:", stack[0] )