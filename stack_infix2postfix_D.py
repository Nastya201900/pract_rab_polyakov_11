
data = "(5+15*(3+8))/(4+(7-1))"
print( "Выражение:", data)

ops = [ '+', '-', '*', '/' ]
priority = { '+': 1, '-': 1,
             '*': 2, '/': 2 }

stack = []
postfix = ''

i = 0
while i < len(data):
  c = data[i]
  i += 1
  if c == '(':            # добавляем открывающую скобку
    stack.append('(')
  elif c == ')':          # снимаем все знаки до ближайшей открывающей
    while stack and stack[-1] != '(':
      postfix += stack.pop() + " "
    stack.pop()
  elif c not in ops:      # записываем число (многозначное)
    postfix += c
    while i < len(data) and data[i].isdigit():
      postfix += data[i]
      i += 1
    postfix += " "
  else:                   # знак операции
    while stack and stack[-1] != '(' and \
          priority[c] <= priority[stack[-1]]:
      postfix += stack.pop() + " "
    stack.append(c)
  print( c, stack, postfix )

while stack:
  postfix += stack.pop() + " "

print ( "Постфиксная форма:", postfix )